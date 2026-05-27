-- ==========================================================
-- V2 - Migration 001
-- Foundation Layer
-- Independent Parent Tables
-- ==========================================================

-- ==========================================================

-- USERS
-- ==========================================================
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    country_of_origin VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- ==========================================================
-- DOCUMENT TYPES
-- ==========================================================
CREATE TABLE document_types (
    document_type_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    global_category VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT check_document_category CHECK (
        global_category IN (
            'University',
            'Career',
            'Relocation'
        )
    )
);

-- ==========================================================
-- EXPENSE CATEGORIES
-- ==========================================================
CREATE TABLE expense_categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- ==========================================================
-- UNIVERSITIES
-- ==========================================================
CREATE TABLE universities (
    university_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    university_type VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    ranking INT,
    website VARCHAR(2083),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    CONSTRAINT check_positive_rank CHECK (ranking > 0 OR ranking IS NULL),
    CONSTRAINT check_university_type CHECK (university_type IN ('Public', 'Private', 'Other'))
);

-- ==========================================================
-- COMPANIES
-- ==========================================================
CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    industry VARCHAR(150),
    country VARCHAR(100),
    website VARCHAR(2083),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);













































-- -- =======================================================================================
-- -- SYSTEM EXTENSIONS & SHARED AUTOMATION ENGINE
-- -- =======================================================================================

-- -- Global function to natively enforce timezone-aware updated_at modifiers across all entities
-- CREATE OR REPLACE FUNCTION set_updated_at_timestamp()
-- RETURNS TRIGGER AS $$
-- BEGIN
--     NEW.updated_at = CURRENT_TIMESTAMP;
--     RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;

-- -- =======================================================================================
-- -- LAYER 1: GLOBAL ENUMS & LOOKUP TABLES (Zero External Dependencies)
-- -- =======================================================================================

-- CREATE TYPE document_category AS ENUM ('University', 'Career', 'Relocation');
-- CREATE TYPE portfolio_item_type AS ENUM ('Skill', 'Project', 'Certificate', 'Language', 'Experience', 'Education');
-- CREATE TYPE uni_app_status AS ENUM ('Preparing', 'Submitted', 'Interviewing', 'Admitted', 'Rejected', 'Withdrawn');
-- CREATE TYPE job_app_status AS ENUM ('Applied', 'Online Assessment', 'Interviewing', 'Offered', 'Rejected', 'Withdrawn');
-- CREATE TYPE file_status AS ENUM ('Active', 'Expired', 'Draft', 'Archived');
-- CREATE TYPE event_classification AS ENUM ('Deadline', 'Appointment', 'Task', 'Interview', 'Flight');
-- CREATE TYPE event_urgency AS ENUM ('Low', 'Medium', 'High', 'Critical');
-- CREATE TYPE event_progress AS ENUM ('Pending', 'In Progress', 'Completed', 'Missed');
-- CREATE TYPE tender_type AS ENUM ('Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'PayPal');

-- CREATE TABLE users (
--     user_id SERIAL PRIMARY KEY,
--     full_name VARCHAR(100) NOT NULL,
--     email VARCHAR(150) UNIQUE NOT NULL,
--     country_of_origin VARCHAR(100) NOT NULL,
--     date_of_birth DATE NOT NULL,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- CREATE TABLE document_types (
--     document_type_id SERIAL PRIMARY KEY,
--     name VARCHAR(100) UNIQUE NOT NULL,
--     global_category document_category NOT NULL,
--     description TEXT,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- CREATE TABLE expense_categories (
--     category_id SERIAL PRIMARY KEY,
--     name VARCHAR(100) UNIQUE NOT NULL,
--     description TEXT,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- CREATE TABLE universities (
--     university_id SERIAL PRIMARY KEY,
--     name VARCHAR(255) UNIQUE NOT NULL,
--     country VARCHAR(100) NOT NULL DEFAULT 'Germany',
--     ranking INT CHECK (ranking > 0),
--     website VARCHAR(2083),
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- CREATE TABLE companies (
--     company_id SERIAL PRIMARY KEY,
--     name VARCHAR(255) UNIQUE NOT NULL,
--     industry VARCHAR(150),
--     country VARCHAR(100),
--     website VARCHAR(2083),
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- -- =======================================================================================
-- -- LAYER 2: SECONDARY MASTER TABLES (Single Parent Dependencies)
-- -- =======================================================================================

-- CREATE TABLE user_portfolio (
--     portfolio_id SERIAL PRIMARY KEY,
--     user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
--     item_type portfolio_item_type NOT NULL,
--     title VARCHAR(150) NOT NULL,
--     summary TEXT,
--     skills_text TEXT, 
--     credential_url VARCHAR(2083),
--     start_date DATE,
--     end_date DATE,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     CONSTRAINT check_portfolio_dates CHECK (end_date >= start_date OR end_date IS NULL)
-- );

-- CREATE TABLE programs (
--     program_id SERIAL PRIMARY KEY,
--     university_id INT NOT NULL REFERENCES universities(university_id) ON DELETE CASCADE,
--     name VARCHAR(255) NOT NULL,
--     degree VARCHAR(50) NOT NULL, 
--     field_of_study VARCHAR(150) NOT NULL,
--     duration_semesters INT NOT NULL CHECK (duration_semesters > 0),
--     tuition_fee NUMERIC(12, 2) DEFAULT 0.00 NOT NULL CHECK (tuition_fee >= 0.00),
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     CONSTRAINT unique_uni_program UNIQUE (university_id, name, degree)
-- );

-- CREATE TABLE intakes (
--     intake_id SERIAL PRIMARY KEY,
--     university_id INT NOT NULL REFERENCES universities(university_id) ON DELETE CASCADE,
--     name VARCHAR(100) NOT NULL, 
--     start_month VARCHAR(20) NOT NULL,
--     application_deadline DATE NOT NULL,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- CREATE TABLE jobs (
--     job_id SERIAL PRIMARY KEY,
--     company_id INT NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE,
--     title VARCHAR(255) NOT NULL,
--     description TEXT,
--     location VARCHAR(150),
--     job_type VARCHAR(50) CHECK (job_type IN ('Full-time', 'Part-time', 'Working Student', 'Internship')),
--     posted_date DATE,
--     source_url VARCHAR(2083),
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- -- =======================================================================================
-- -- LAYER 3: CORE WORKFLOW INTERSECTIONS (Multi-Parent Application Trackers)
-- -- =======================================================================================

-- CREATE TABLE university_applications (
--     application_id SERIAL PRIMARY KEY,
--     user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
--     university_id INT NOT NULL REFERENCES universities(university_id) ON DELETE RESTRICT,
--     program_id INT NOT NULL REFERENCES programs(program_id) ON DELETE RESTRICT,
--     intake_id INT NOT NULL REFERENCES intakes(intake_id) ON DELETE RESTRICT,
--     application_date DATE DEFAULT CURRENT_DATE NOT NULL,
--     status uni_app_status NOT NULL DEFAULT 'Preparing',
--     stage VARCHAR(50), 
--     decision_date DATE,
--     notes TEXT,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     CONSTRAINT unique_user_program_intake UNIQUE (user_id, program_id, intake_id)
-- );

-- CREATE TABLE job_applications (
--     job_application_id SERIAL PRIMARY KEY,
--     user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
--     job_id INT NOT NULL REFERENCES jobs(job_id) ON DELETE RESTRICT,
--     applied_date DATE DEFAULT CURRENT_DATE NOT NULL,
--     status job_app_status NOT NULL DEFAULT 'Applied',
--     notes TEXT,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     CONSTRAINT unique_user_job UNIQUE (user_id, job_id)
-- );

-- -- =======================================================================================
-- -- LAYER 4: OPERATIONAL PIPELINES & TIME-SERIES CALENDARS
-- -- =======================================================================================

-- CREATE TABLE documents (
--     document_id SERIAL PRIMARY KEY,
--     user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
--     document_type_id INT NOT NULL REFERENCES document_types(document_type_id) ON DELETE RESTRICT,
--     file_name VARCHAR(255) NOT NULL,
--     file_path VARCHAR(512) NOT NULL,
--     upload_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     expiry_date DATE,
--     status file_status DEFAULT 'Active' NOT NULL,
--     notes TEXT,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- CREATE TABLE calendar_events (
--     event_id SERIAL PRIMARY KEY,
--     user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
--     title VARCHAR(205) NOT NULL,
--     description TEXT,
--     event_type event_classification NOT NULL,
--     start_datetime TIMESTAMPTZ NOT NULL,
--     end_datetime TIMESTAMPTZ NOT NULL,
--     location VARCHAR(255),
--     priority event_urgency DEFAULT 'Medium' NOT NULL,
--     status event_progress DEFAULT 'Pending' NOT NULL,
--     notes TEXT,
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     CONSTRAINT check_event_dates CHECK (end_datetime >= start_datetime)
-- );

-- -- =======================================================================================
-- -- LAYER 5: THE UNIFIED FINANCIAL OVERHEAD CAPITAL LEDGER
-- -- =======================================================================================

-- CREATE TABLE journey_expenses (
--     expense_id SERIAL PRIMARY KEY,
--     user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
--     category_id INT NOT NULL REFERENCES expense_categories(category_id) ON DELETE RESTRICT,
--     document_id INT REFERENCES documents(document_id) ON DELETE SET NULL,
--     university_application_id INT REFERENCES university_applications(application_id) ON DELETE SET NULL,
--     job_application_id INT REFERENCES job_applications(job_application_id) ON DELETE SET NULL,
--     calendar_event_id INT REFERENCES calendar_events(event_id) ON DELETE SET NULL,
--     title VARCHAR(150) NOT NULL,
--     description TEXT,
--     amount NUMERIC(12, 2) NOT NULL CHECK (amount >= 0.00),
--     currency VARCHAR(10) DEFAULT 'EUR' NOT NULL,
--     expense_date DATE DEFAULT CURRENT_DATE NOT NULL,
--     payment_method tender_type,
--     notes TEXT,
--     receipt_path VARCHAR(512),
--     created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
--     updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
-- );

-- -- =======================================================================================
-- -- AUTOMATED COOLDOWN WATCHERS (Database Row Trigger Registration)
-- -- =======================================================================================

-- CREATE TRIGGER rx_users BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_doc_types BEFORE UPDATE ON document_types FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_exp_categories BEFORE UPDATE ON expense_categories FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_universities BEFORE UPDATE ON universities FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_companies BEFORE UPDATE ON companies FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_portfolio BEFORE UPDATE ON user_portfolio FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_programs BEFORE UPDATE ON programs FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_intakes BEFORE UPDATE ON intakes FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_jobs BEFORE UPDATE ON jobs FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_uni_apps BEFORE UPDATE ON university_applications FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_job_apps BEFORE UPDATE ON job_applications FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_documents BEFORE UPDATE ON documents FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_calendar BEFORE UPDATE ON calendar_events FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();
-- CREATE TRIGGER rx_expenses BEFORE UPDATE ON journey_expenses FOR EACH ROW EXECUTE FUNCTION set_updated_at_timestamp();

-- -- =======================================================================================
-- -- PERFORMANCE TUNING: COMPOSITE CONCURRENCY INDEXES
-- -- =======================================================================================

-- CREATE INDEX idx_user_portfolio_lookup ON user_portfolio (user_id, item_type);
-- CREATE INDEX idx_program_mapping ON programs (university_id, degree);
-- CREATE INDEX idx_uni_applications_dashboard ON university_applications (user_id, status);
-- CREATE INDEX idx_job_applications_dashboard ON job_applications (user_id, status);
-- CREATE INDEX idx_documents_routing ON documents (user_id, document_type_id);
-- CREATE INDEX idx_calendar_timeline ON calendar_events (user_id, start_datetime, end_datetime);
-- CREATE INDEX idx_expenses_ledger ON journey_expenses (user_id, category_id, expense_date);