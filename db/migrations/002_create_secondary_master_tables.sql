-- ==========================================================
-- V2 - Migration 002
-- Secondary Master Tables
-- Single Parent Dependencies
-- ==========================================================

BEGIN;

-- ==========================================================
-- 1. USER PORTFOLIO
-- ==========================================================

CREATE TABLE user_portfolio (
    portfolio_id SERIAL PRIMARY KEY,

    user_id INT NOT NULL
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    item_type VARCHAR(50) NOT NULL,

    title VARCHAR(150) NOT NULL,

    summary TEXT,

    skills_text TEXT,

    credential_url VARCHAR(2083),

    start_date DATE,

    end_date DATE,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT check_portfolio_item_type
    CHECK (
        item_type IN (
            'Skill',
            'Project',
            'Certificate',
            'Language',
            'Experience',
            'Education'
        )
    ),

    CONSTRAINT check_portfolio_dates
    CHECK (
        end_date IS NULL
        OR end_date >= start_date
    )
);



-- ==========================================================
-- 2. UNIVERSITY PROGRAMS
-- ==========================================================

CREATE TABLE programs (
    program_id SERIAL PRIMARY KEY,

    university_id INT NOT NULL
        REFERENCES universities(university_id)
        ON DELETE CASCADE,

    name VARCHAR(255) NOT NULL,

    degree VARCHAR(50) NOT NULL,

    field_of_study VARCHAR(150) NOT NULL,

    duration_semesters INT NOT NULL,

    tuition_fee NUMERIC(12,2)
        DEFAULT 0.00
        NOT NULL,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT check_duration_positive
    CHECK (
        duration_semesters > 0
    ),

    CONSTRAINT check_tuition_positive
    CHECK (
        tuition_fee >= 0.00
    ),

    CONSTRAINT unique_uni_program
    UNIQUE (
        university_id,
        name,
        degree
    )
);



-- ==========================================================
-- 3. UNIVERSITY INTAKES
-- ==========================================================

CREATE TABLE intakes (
    intake_id SERIAL PRIMARY KEY,

    university_id INT NOT NULL
        REFERENCES universities(university_id)
        ON DELETE CASCADE,

    name VARCHAR(100) NOT NULL,

    start_month VARCHAR(20) NOT NULL,

    application_deadline DATE NOT NULL,

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);



-- ==========================================================
-- 4. JOBS / VACANCIES
-- ==========================================================

CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,

    company_id INT NOT NULL
        REFERENCES companies(company_id)
        ON DELETE CASCADE,

    title VARCHAR(255) NOT NULL,

    description TEXT,

    location VARCHAR(150),

    job_type VARCHAR(50),

    posted_date DATE,

    source_url VARCHAR(2083),

    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT check_job_type
    CHECK (
        job_type IN (
            'Full-time',
            'Part-time',
            'Working Student',
            'Internship'
        )
        OR job_type IS NULL
    )
);

COMMIT;