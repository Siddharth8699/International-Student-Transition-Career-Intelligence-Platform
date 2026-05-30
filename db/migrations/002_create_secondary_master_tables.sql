-- =======================================================================================
-- V2 - Migration 002: Secondary Master Tables (Single Parent Dependencies)
-- =======================================================================================

BEGIN;

-- =======================================================================================
-- 1. USER PORTFOLIO / RESUME SNAPSHOT
-- =======================================================================================
CREATE TABLE user_profiles (
    profile_id   SERIAL PRIMARY KEY,
    user_id      INT NOT NULL UNIQUE,
    headline     VARCHAR(255),
    summary      TEXT,
    education    TEXT,
    experience   TEXT,
    projects     TEXT,
    skills       TEXT,
    languages    TEXT,
    certificates TEXT,
    resume_url   VARCHAR(2083) NOT NULL,
    created_at   TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at   TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT fk_user_profile FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- =======================================================================================
-- 2. UNIVERSITY PROGRAMS
-- =======================================================================================
CREATE TABLE programs (
    program_id         SERIAL PRIMARY KEY,
    university_id      INT NOT NULL,
    name               VARCHAR(255) NOT NULL,
    degree             VARCHAR(50) NOT NULL,
    field_of_study     VARCHAR(150) NOT NULL,
    duration_semesters INT NOT NULL,
    tuition_fee        NUMERIC(12,2) NOT NULL,
    
    -- Your New Requirement Link
    requirement_url    VARCHAR(500) NOT NULL,
    
    created_at         TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at         TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    -- Safety Constraints
    CONSTRAINT fk_program_university 
        FOREIGN KEY (university_id) 
        REFERENCES universities(university_id) 
        ON DELETE CASCADE,

    CONSTRAINT check_degree_type 
        CHECK (degree IN ('Bachelor', 'Master', 'PhD', 'Diploma', 'Certificate', 'Foundation', 'Other')),

    CONSTRAINT check_duration_positive 
        CHECK (duration_semesters > 0),

    CONSTRAINT check_tuition_positive 
        CHECK (tuition_fee >= 0.00),

    CONSTRAINT unique_uni_program 
        UNIQUE (university_id, name, degree)
);

-- =======================================================================================
-- 3. UNIVERSITY INTAKES
-- =======================================================================================
CREATE TABLE intakes (
    intake_id            SERIAL PRIMARY KEY,
    program_id           INT NOT NULL,
    name                 VARCHAR(50) NOT NULL,
    start_month          VARCHAR(20) NOT NULL,
    application_deadline DATE NOT NULL,
    created_at           TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at           TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT fk_intake_program 
        FOREIGN KEY (program_id) 
        REFERENCES programs(program_id) 
        ON DELETE CASCADE,

    CONSTRAINT check_intake_type 
        CHECK (name IN ('Winter', 'Summer', 'Spring', 'Fall')),

    CONSTRAINT check_start_month 
        CHECK (start_month IN (
            'January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August', 'September', 'October', 'November', 'December'
        )),

    CONSTRAINT unique_program_intake 
        UNIQUE (program_id, name)
);

-- =======================================================================================
-- 4. CORPORATE VACANCIES / JOBS
-- =======================================================================================

CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    location VARCHAR(150),
    description TEXT,
    location VARCHAR(150),
    work_mode VARCHAR(30),
    job_type VARCHAR(50),
    salary_min NUMERIC(12,2),
    salary_max NUMERIC(12,2),
    currency VARCHAR(10),
    posted_date DATE NOT NULL,
    application_deadline DATE,
    source_url VARCHAR(2083) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT check_job_type CHECK (
        job_type IN (
            'Full-time',
            'Part-time',
            'Working Student',
            'Internship',
            'Contract'
        )
    ),

    CONSTRAINT check_work_mode CHECK (
        work_mode IN (
            'Onsite',
            'Hybrid',
            'Remote'
        )
    ),

    CONSTRAINT check_salary_range CHECK (
        salary_min IS NULL
        OR salary_max IS NULL
        OR salary_min <= salary_max
    )
);

-- =======================================================================================
-- 5. USER DOCUMENT CHECKLIST (Updated with Surrogate Tracking ID & Unique Gatekeeper)
-- =======================================================================================

CREATE TABLE user_documents_checklist (
    id               SERIAL PRIMARY KEY,                     -- Your simple, sequential tracking ID
    user_id          INT NOT NULL,
    document_type_id INT NOT NULL,
    is_ready         BOOLEAN DEFAULT FALSE NOT NULL,
    
    -- Added tracking timestamps
    created_at       TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at       TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    -- THE GATEKEEPER: Ensures uniqueness for the user + document combination
    CONSTRAINT unique_user_document UNIQUE (user_id, document_type_id),
    
    CONSTRAINT fk_checklist_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    CONSTRAINT fk_checklist_type FOREIGN KEY (document_type_id) REFERENCES document_types(document_type_id) ON DELETE RESTRICT
);


-- =======================================================================================
-- 6. USER READINESS 
-- =======================================================================================

CREATE TABLE user_readiness_cache (
    user_id              INT PRIMARY KEY,
    has_passport         BOOLEAN DEFAULT FALSE NOT NULL,
    has_transcripts      BOOLEAN DEFAULT FALSE NOT NULL,
    has_bachelors_degree BOOLEAN DEFAULT FALSE NOT NULL,
    has_highschool_cert  BOOLEAN DEFAULT FALSE NOT NULL,
    has_aps_certificate  BOOLEAN DEFAULT FALSE NOT NULL,
    has_resume           BOOLEAN DEFAULT FALSE NOT NULL,
    has_cover_letter     BOOLEAN DEFAULT FALSE NOT NULL,
    has_language_proof   BOOLEAN DEFAULT FALSE NOT NULL,
    
    ready_for_uni        BOOLEAN GENERATED ALWAYS AS (
        has_passport AND has_transcripts AND has_bachelors_degree AND has_highschool_cert AND has_aps_certificate AND has_resume AND has_language_proof
    ) STORED NOT NULL,
    
    ready_for_job        BOOLEAN GENERATED ALWAYS AS (
        has_resume AND has_passport AND has_cover_letter
    ) STORED NOT NULL,
    
    -- Added tracking timestamps
    created_at           TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at           TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    CONSTRAINT fk_readiness_user FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);


-- =========================================================================
-- CREATE THE TRIGGER FUNCTION (Step A)
-- =========================================================================

CREATE OR REPLACE FUNCTION sync_user_readiness_cache()
RETURNS TRIGGER AS $$
DECLARE
    v_doc_name VARCHAR(100);
    v_column_name TEXT;
BEGIN
    SELECT name INTO v_doc_name FROM document_types WHERE document_type_id = NEW.document_type_id;

    CASE v_doc_name
        WHEN 'Passport'               THEN v_column_name := 'has_passport';
        WHEN 'Transcript'             THEN v_column_name := 'has_transcripts';
        WHEN 'Bachelor Degree'         THEN v_column_name := 'has_bachelors_degree';
        WHEN 'Highschool Certificate'  THEN v_column_name := 'has_highschool_cert';
        WHEN 'APS Certificate'         THEN v_column_name := 'has_aps_certificate';
        WHEN 'Resume'                  THEN v_column_name := 'has_resume';
        WHEN 'Cover Letter'            THEN v_column_name := 'has_cover_letter';
        WHEN 'Language Proof'          THEN v_column_name := 'has_language_proof';
        ELSE RETURN NEW;
    END CASE;

    EXECUTE format(
        'INSERT INTO user_readiness_cache (user_id, %I) VALUES ($1, $2) ' ||
        'ON CONFLICT (user_id) DO UPDATE SET %I = $2, updated_at = CURRENT_TIMESTAMP;', 
        v_column_name, v_column_name
    ) USING NEW.user_id, NEW.is_ready;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- =========================================================================
-- ATTACH THE TRIGGER TO THE TABLE (Step B - Goes immediately after Step A)
-- =========================================================================

CREATE TRIGGER trg_sync_readiness_cache
AFTER INSERT OR UPDATE ON user_documents_checklist
FOR EACH ROW
EXECUTE FUNCTION sync_user_readiness_cache();


COMMIT;