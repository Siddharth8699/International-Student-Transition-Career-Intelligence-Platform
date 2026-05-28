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

    CONSTRAINT fk_user_profile 
        FOREIGN KEY (user_id) 
        REFERENCES users(user_id) 
        ON DELETE CASCADE
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
    created_at         TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at         TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

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


COMMIT;