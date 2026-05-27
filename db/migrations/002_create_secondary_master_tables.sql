-- =======================================================================================
-- V2 - Migration 002: Secondary Master Tables (Single Parent Dependencies)
-- =======================================================================================

BEGIN;

-- ==========================================================
-- 1. USER PORTFOLIO
-- ==========================================================
CREATE TABLE user_profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL UNIQUE REFERENCES users(user_id) ON DELETE CASCADE,
    headline VARCHAR(255),
    summary TEXT,
    education TEXT,
    experience TEXT,
    projects TEXT,
    skills TEXT,
    languages TEXT,
    certificates TEXT,
    resume_url VARCHAR(2083) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- ==========================================================
-- 2. UNIVERSITY PROGRAMS
-- ==========================================================
CREATE TABLE programs (
    program_id SERIAL PRIMARY KEY,
    university_id INT NOT NULL REFERENCES universities(university_id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    degree VARCHAR(50) NOT NULL,
    field_of_study VARCHAR(150) NOT NULL,
    duration_semesters INT NOT NULL,
    tuition_fee NUMERIC(12,2) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    CONSTRAINT check_duration_positive CHECK (duration_semesters > 0),
    CONSTRAINT check_tuition_positive CHECK (tuition_fee >= 0.00),
    CONSTRAINT unique_uni_program UNIQUE (university_id, name, degree)
);

-- ==========================================================
-- 3. UNIVERSITY INTAKES
-- ==========================================================
CREATE TABLE intakes (
    intake_id SERIAL PRIMARY KEY,
    program_id INT NOT NULL
    REFERENCES programs(program_id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    start_month VARCHAR(20) NOT NULL,
    application_deadline DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT unique_program_intake UNIQUE (program_id, name)
);

-- ==========================================================
-- 4. JOBS
-- ==========================================================
CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    company_id INT NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(150),
    job_type VARCHAR(50),
    posted_date DATE,
    source_url VARCHAR(2083),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    CONSTRAINT check_job_type CHECK (
        job_type IN ('Full-time', 'Part-time', 'Working Student', 'Internship') OR job_type IS NULL
    )
);

COMMIT;