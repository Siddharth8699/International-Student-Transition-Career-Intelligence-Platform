BEGIN;

-- =======================================================================================
-- LAYER 2: DEPENDENT TRANSACTIONAL TABLES
-- =======================================================================================

-- 1. USER PROFILES (1:1 with users table via user_id 1, 2, 3)
INSERT INTO user_profiles (user_id, headline, summary, education, experience, projects, skills, languages, certificates, resume_url) VALUES
(1, 'Backend Engineering Student', 'Preparing for international education and backend opportunities.', 'B.Tech Computer Science', 'Junior Backend Developer', 'International Student Transition Platform, Portfolio CLI System', 'Python, PostgreSQL, SQL, Git', 'English C1, German A2', 'Goethe A2', 'https://resume.example.com/siddharth'),
(2, 'Data & Automation Enthusiast', 'Interested in analytics and automation workflows.', 'Bachelor of Information Systems', NULL, 'Automated Portfolio Tracker', 'Python, SQLite, JSON, Pandas', 'English B2, Ukrainian Native', NULL, 'https://resume.example.com/elena'),
(3, 'Cloud & Backend Engineering Candidate', 'Building cloud and backend capabilities.', 'Bachelor of Software Engineering', NULL, 'Cloud Deployment Sandbox', 'AWS, Python, Security', 'Spanish Native, English B2', 'AWS Certified Cloud Practitioner', 'https://resume.example.com/carlos');

-- 2. UNIVERSITY PROGRAMS (Linked to university_id. Degrees fixed to match strict CHECK constraint)
INSERT INTO programs (university_id, name, degree, field_of_study, duration_semesters, tuition_fee, requirement_url) VALUES
(1, 'Computer Science', 'Master', 'Informatics and Data Engineering', 4, 0.00, 'https://example.com/uni1/cs-requirements'),
(1, 'Global Production Engineering', 'Master', 'Engineering Management', 4, 15500.00, 'https://example.com/uni1/gpe-requirements'),
(2, 'Software Systems Engineering', 'Master', 'Computer Science & Software Architecture', 4, 0.00, 'https://example.com/uni2/sse-requirements'),
(2, 'Automotive Engineering', 'Master', 'Mechanical Engineering', 3, 0.00, 'https://example.com/uni2/auto-requirements'),
(3, 'Informatics', 'Master', 'Advanced Computer Science & AI', 4, 0.00, 'https://example.com/uni3/informatics-requirements'),
(3, 'Data Engineering and Analytics', 'Master', 'Big Data Technologies', 4, 0.00, 'https://example.com/uni3/data-requirements'),
(8, 'International Business', 'Bachelor', 'Global Commerce & Management', 6, 6200.00, 'https://example.com/uni8/ib-requirements');

-- 3. UNIVERSITY INTAKES (Linked cleanly to valid program_id numbers 1 to 7)
INSERT INTO intakes (program_id, name, start_month, application_deadline) VALUES
(1, 'Winter', 'October', '2026-05-31'), -- Linked to CS (TU Berlin)
(1, 'Summer', 'April', '2026-10-31'),   -- Linked to CS (TU Berlin)
(2, 'Winter', 'October', '2026-03-01'), -- Linked to Global Production (TU Berlin)
(3, 'Winter', 'September', '2026-06-15'), -- Linked to Software Systems (RWTH Aachen)
(3, 'Summer', 'March', '2026-01-15'),   -- Linked to Software Systems (RWTH Aachen)
(5, 'Winter', 'October', '2026-05-31'), -- Linked to Informatics (TUM)
(6, 'Winter', 'October', '2026-05-31'), -- Linked to Data Eng (TUM)
(7, 'Fall', 'September', '2026-07-15'); -- Linked to Business (SRH)

-- 4. CORPORATE VACANCIES / JOBS (Linked to valid company_id values)
INSERT INTO jobs (company_id, title, description, location, work_mode, job_type, salary_min, salary_max, currency, posted_date, application_deadline, source_url) VALUES
(1, 'Backend Engineering Working Student', 'Assist team in optimizing internal relational data workflows and testing Python script wrappers.', 'Munich, Germany', 'Hybrid', 'Working Student', NULL, NULL, 'EUR', '2026-05-20', '2026-06-20', 'https://jobs.siemens.com/vacancies/1092'),
(1, 'Automation Systems Intern', 'Full-time internship focused on supporting engineering lifecycle simulations.', 'Erlangen, Germany', 'Onsite', 'Internship', NULL, NULL, 'EUR', '2026-05-22', '2026-06-22', 'https://jobs.siemens.com/vacancies/1145'),
(2, 'Junior Cloud Developer', 'Full-time role focused on developing and maintaining platform microservices.', 'Walldorf, Germany', 'Hybrid', 'Full-time', 55000.00, 70000.00, 'EUR', '2026-05-18', '2026-06-18', 'https://jobs.sap.com/vacancies/8834'),
(2, 'Data Analytics Intern', 'Part-time data extraction role helping build enterprise report dashboards.', 'Berlin, Germany', 'Remote', 'Internship', NULL, NULL, 'EUR', '2026-05-24', '2026-06-24', NULL);

--5 user_document_checklist
INSERT INTO user_documents_checklist (user_id, document_type_id, is_ready) VALUES
-- ==========================================
-- USER 1: Fully Ready (Has everything)
-- ==========================================
(1, 1, TRUE),  -- Passport
(1, 2, TRUE),  -- Transcript
(1, 3, TRUE),  -- Bachelor Degree
(1, 4, TRUE),  -- Highschool Certificate
(1, 5, TRUE),  -- APS Certificate
(1, 6, TRUE),  -- Resume
(1, 7, TRUE),  -- Cover Letter
(1, 8, TRUE),  -- Language Proof

-- ==========================================
-- USER 2: Academic Ready Only (Missing Career pieces)
-- ==========================================
(2, 1, TRUE),  -- Passport
(2, 2, TRUE),  -- Transcript
(2, 3, TRUE),  -- Bachelor Degree
(2, 4, TRUE),  -- Highschool Certificate
(2, 5, TRUE),  -- APS Certificate
(2, 6, TRUE),  -- Resume
(2, 7, FALSE), -- Cover Letter (Not ready)
(2, 8, TRUE),  -- Language Proof

-- ==========================================
-- USER 3: Just Starting Out (Most things are FALSE)
-- ==========================================
(3, 1, TRUE),  -- Passport (They have their ID ready)
(3, 2, FALSE), -- Transcript
(3, 3, FALSE), -- Bachelor Degree
(3, 4, FALSE), -- Highschool Certificate
(3, 5, FALSE), -- APS Certificate
(3, 6, TRUE),  -- Resume (They draft a CV)
(3, 7, FALSE), -- Cover Letter
(3, 8, FALSE)  -- Language Proof

ON CONFLICT (user_id, document_type_id) DO NOTHING;



COMMIT;