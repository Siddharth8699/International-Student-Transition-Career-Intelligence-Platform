-- ==========================================================================
-- STEP 0: CLEAN SLATE DEPENDENCY RESET
-- ==========================================================================
DROP VIEW IF EXISTS v_dashboard_intake_milestones CASCADE;
DROP VIEW IF EXISTS v_dashboard_application_watchlist CASCADE;
DROP VIEW IF EXISTS v_dashboard_application_analytics_summary CASCADE;
DROP VIEW IF EXISTS university_pipeline_summary CASCADE;

-- ==========================================================================
-- STEP 1: TABLES CONFIGURATION
-- ==========================================================================

-- 1.1: Application Status Lookup Table
CREATE TABLE IF NOT EXISTS application_statuses (
    application_status_id SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE
);

-- 1.2: Core Application Log Table
CREATE TABLE IF NOT EXISTS university_applications (
    university_application_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    intake_id INT NOT NULL,
    status_id INT NOT NULL DEFAULT 1,
    application_guidance_token VARCHAR(100) NOT NULL,
    target_year INT NOT NULL DEFAULT 2026,
    application_platform VARCHAR(50),
    platform_url TEXT,
    notes TEXT,
    applied_date DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,

    CONSTRAINT fk_application_status 
        FOREIGN KEY (status_id) REFERENCES application_statuses(application_status_id),
    CONSTRAINT unique_user_intake_status 
        UNIQUE (user_id, intake_id, status_id)
);

-- 1.3: History Log Audit Table
CREATE TABLE IF NOT EXISTS university_application_history (
    university_application_history_id SERIAL PRIMARY KEY,
    university_application_id          INT NOT NULL,
    status_id                          INT NOT NULL,
    notes                              TEXT,
    changed_at                         TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    
    CONSTRAINT fk_history_parent_application
        FOREIGN KEY (university_application_id) 
        REFERENCES university_applications(university_application_id) 
        ON DELETE CASCADE,
    CONSTRAINT fk_history_status
        FOREIGN KEY (status_id) REFERENCES application_statuses(application_status_id)
);

-- ==========================================================================
-- STEP 2: AUTOMATED AUDIT TRIGGER ENGINE
-- ==========================================================================

CREATE OR REPLACE FUNCTION log_university_application_status_change()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO university_application_history (university_application_id, status_id, notes)
        VALUES (NEW.university_application_id, NEW.status_id, 'Application initialized.');
    ELIF TG_OP = 'UPDATE' THEN
        IF OLD.status_id IS DISTINCT FROM NEW.status_id THEN
            INSERT INTO university_application_history (university_application_id, status_id, notes)
            VALUES (NEW.university_application_id, NEW.status_id, 'Status updated.');
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trigger_track_university_application_history ON university_applications;

CREATE TRIGGER trigger_track_university_application_history
AFTER INSERT OR UPDATE ON university_applications
FOR EACH ROW
EXECUTE FUNCTION log_university_application_status_change();

-- ==========================================================================
-- STEP 3: DASHBOARD METRICS VIEWS
-- ==========================================================================

-- 3.1: High-Level Pipeline Summary Metrics
CREATE OR REPLACE VIEW university_pipeline_summary AS
WITH latest_application_states AS (
    SELECT DISTINCT ON (university_application_id) 
        university_application_id, 
        status_id
    FROM university_application_history
    ORDER BY university_application_id, changed_at DESC
),
total_history_stats AS (
    SELECT COUNT(university_application_id) AS total_historical_applications
    FROM university_applications
)
SELECT 
    (SELECT total_historical_applications FROM total_history_stats) AS total_historical_count,
    COUNT(l.university_application_id) AS current_active_total,
    COUNT(l.university_application_id) FILTER (WHERE l.status_id = 1) AS current_applied,
    COUNT(l.university_application_id) FILTER (WHERE l.status_id = 4) AS current_accepted,
    COALESCE(
        ROUND(
            (COUNT(l.university_application_id) FILTER (WHERE l.status_id = 4))::NUMERIC / 
            NULLIF(COUNT(l.university_application_id) FILTER (WHERE l.status_id IN (1, 4)), 0) * 100, 
            2
        ), 
        0.00
    ) AS success_rate_percentage
FROM latest_application_states l;

-- 3.2: Strategic Target Analytics Overview (Aggregated JSON Dimensions)
CREATE OR REPLACE VIEW v_dashboard_application_analytics_summary AS
WITH latest_status AS (
    SELECT DISTINCT ON (university_application_id) 
        university_application_id, 
        status_id
    FROM university_application_history
    ORDER BY university_application_id, changed_at DESC
),
base_query AS (
    SELECT 
        u.name as university_name,
        p.program_id,
        p.name AS program_name,
        p.degree AS program_degree,
        ua.university_application_id,
        CASE 
            WHEN ua.application_platform ILIKE '%assist%' 
              OR ua.application_platform ILIKE '%uni%' THEN 'Uni-Assist' 
            ELSE 'University Portal' 
        END AS standardized_platform,
        ls.status_id
    FROM universities u
    LEFT JOIN programs p ON u.university_id = p.university_id
    LEFT JOIN intakes ip ON p.program_id = ip.program_id
    LEFT JOIN university_applications ua ON ip.intake_id = ua.intake_id
    LEFT JOIN latest_status ls ON ua.university_application_id = ls.university_application_id
),
university_math AS (
    SELECT 
        university_name,
        COUNT(university_application_id) AS total_submissions,
        COALESCE(ROUND((COUNT(university_application_id) FILTER (WHERE status_id = 4))::NUMERIC / NULLIF(COUNT(university_application_id) FILTER (WHERE status_id IN (4, 5)), 0) * 100, 2), 0.00) AS success_rate
    FROM base_query
    GROUP BY university_name
),
university_block AS (
    SELECT json_agg(json_build_object(
        'university_name', university_name,
        'total_submissions', total_submissions,
        'success_rate', success_rate
    )) AS university_data
    FROM university_math
),
program_math AS (
    SELECT 
        program_name,
        program_degree,
        COUNT(university_application_id) AS total_submissions,
        COALESCE(ROUND((COUNT(university_application_id) FILTER (WHERE status_id = 4))::NUMERIC / NULLIF(COUNT(university_application_id) FILTER (WHERE status_id IN (4, 5)), 0) * 100, 2), 0.00) AS success_rate
    FROM base_query
    WHERE program_id IS NOT NULL
    GROUP BY program_name, program_degree
),
program_block AS (
    SELECT json_agg(json_build_object(
        'program_name', program_name,
        'program_degree', program_degree,
        'total_submissions', total_submissions,
        'success_rate', success_rate
    )) AS program_data
    FROM program_math
),
platform_math AS (
    SELECT 
        standardized_platform,
        COUNT(university_application_id) AS total_submissions,
        COALESCE(ROUND((COUNT(university_application_id) FILTER (WHERE status_id = 4))::NUMERIC / NULLIF(COUNT(university_application_id) FILTER (WHERE status_id IN (4, 5)), 0) * 100, 2), 0.00) AS success_rate
    FROM base_query
    WHERE university_application_id IS NOT NULL
    GROUP BY standardized_platform
),
platform_block AS (
    SELECT json_agg(json_build_object(
        'standardized_platform', standardized_platform,
        'total_submissions', total_submissions,
        'success_rate', success_rate
    )) AS platform_data
    FROM platform_math
)
SELECT 
    u.university_data,
    p.program_data,
    pl.platform_data
FROM university_block u
CROSS JOIN program_block p
CROSS JOIN platform_block pl;

-- 3.3: Actionable Watchlist & Long-term Bottlenecks (> 49 Days)
CREATE OR REPLACE VIEW v_dashboard_application_watchlist AS
WITH latest_status AS (
    SELECT DISTINCT ON (university_application_id)
        university_application_id, 
        status_id
    FROM university_application_history
    ORDER BY university_application_id, changed_at DESC
),
base_query AS (
    SELECT 
        u.name AS university_name, 
        p.name AS program_name, 
        ls.status_id, 
        ua.applied_date
    FROM universities AS u 
    JOIN programs AS p ON u.university_id = p.university_id
    JOIN intakes AS i ON p.program_id = i.program_id
    JOIN university_applications AS ua ON i.intake_id = ua.intake_id
    JOIN latest_status AS ls ON ua.university_application_id = ls.university_application_id
    WHERE ls.status_id IN (1, 2)
),
age_block AS (
    SELECT 
        university_name,
        program_name,
        status_id,
        applied_date,
        (CURRENT_DATE - applied_date::DATE) AS elapsed_days
    FROM base_query
)
SELECT * FROM age_block
WHERE elapsed_days > 49;

-- 3.4: Active Intake Term Progress & Cycle Milestones
CREATE OR REPLACE VIEW v_dashboard_intake_milestones AS
WITH latest_status AS (
    SELECT DISTINCT ON (university_application_id)
        university_application_id, 
        status_id
    FROM university_application_history
    ORDER BY university_application_id, changed_at DESC
),
base_query AS (
    SELECT 
        i.name AS intake_name, 
        ua.target_year AS intake_year, 
        ast.status_name AS status_name, 
        ua.university_application_id
    FROM intakes AS i
    JOIN university_applications AS ua ON i.intake_id = ua.intake_id
    JOIN latest_status AS ls ON ua.university_application_id = ls.university_application_id
    JOIN application_statuses AS ast ON ls.status_id = ast.application_status_id
)
SELECT 
    intake_name, 
    intake_year, 
    status_name, 
    COUNT(university_application_id) AS application_count
FROM base_query
GROUP BY intake_name, intake_year, status_name
ORDER BY intake_year DESC, intake_name, status_name;