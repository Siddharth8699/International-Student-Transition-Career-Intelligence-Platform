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
INSERT INTO programs (university_id, name, degree, field_of_study, duration_semesters, tuition_fee) VALUES
(1, 'Computer Science', 'Master', 'Informatics and Data Engineering', 4, 0.00),                       -- program_id = 1
(1, 'Global Production Engineering', 'Master', 'Engineering Management', 4, 15500.00),               -- program_id = 2
(2, 'Software Systems Engineering', 'Master', 'Computer Science & Software Architecture', 4, 0.00),   -- program_id = 3
(2, 'Automotive Engineering', 'Master', 'Mechanical Engineering', 3, 0.00),                           -- program_id = 4
(3, 'Informatics', 'Master', 'Advanced Computer Science & AI', 4, 0.00),                              -- program_id = 5
(3, 'Data Engineering and Analytics', 'Master', 'Big Data Technologies', 4, 0.00),                    -- program_id = 6
(8, 'International Business', 'Bachelor', 'Global Commerce & Management', 6, 6200.00);                -- program_id = 7

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
INSERT INTO jobs (company_id, title, description, location, job_type, posted_date, source_url) VALUES
(1, 'Backend Engineering Working Student', 'Assist team in optimizing internal relational data workflows and testing Python script wrappers.', 'Munich, Germany', 'Working Student', '2026-05-20', 'https://jobs.siemens.com/vacancies/1092'),
(1, 'Automation Systems Intern', 'Full-time internship focused on supporting engineering lifecycle simulations.', 'Erlangen, Germany', 'Internship', '2026-05-22', 'https://jobs.siemens.com/vacancies/1145'),
(2, 'Junior Cloud Developer', 'Full-time role focused on developing and maintaining platform microservices.', 'Walldorf, Germany', 'Full-time', '2026-05-18', 'https://jobs.sap.com/vacancies/8834'),
(2, 'Data Analytics Intern', 'Part-time data extraction role helping build enterprise report dashboards.', 'Berlin, Germany', 'Internship', '2026-05-24', NULL);

COMMIT;