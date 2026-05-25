BEGIN;

-- ==========================================================
-- 1. SEED: USER PORTFOLIO
-- ==========================================================


INSERT INTO user_portfolio (user_id, item_type, title, summary, skills_text, credential_url, start_date, end_date) VALUES
-- Siddharth Dev (user_id = 1)
(1, 'Education', 'B.Tech in Computer Science', 'Completed undergraduate degree focused on software engineering.', 'Python, SQL, Data Structures', 'https://credentials.example.com/sid-btech', '2019-08-01', '2023-05-30'),
(1, 'Experience', 'Junior Backend Developer', 'Developed data pipelines and managed relational databases.', 'PostgreSQL, Django, Git', NULL, '2023-07-01', '2025-12-31'),
(1, 'Language', 'German A2 Certification', 'Passed Goethe-Institut A2 examination.', 'German, Communication', 'https://credentials.example.com/sid-a2', '2025-02-01', '2025-05-15'),

-- Elena Rostova (user_id = 2)
(2, 'Project', 'Automated Portfolio Tracker', 'Built a local terminal application to manage mock user assets.', 'Python, SQLite, JSON', 'https://github.com/elena/portfolio-tracker', '2026-01-10', '2026-02-20'),
(2, 'Skill', 'Advanced Data Analysis', 'Mastered tabular manipulation and statistical aggregation techniques.', 'Pandas, NumPy, Excel', NULL, NULL, NULL),

-- Carlos Mendez (user_id = 3)
(3, 'Certificate', 'AWS Certified Cloud Practitioner', 'Validation of overall understanding of the AWS Cloud platform.', 'AWS, Cloud Computing, Security', 'https://credentials.example.com/carlos-aws', '2024-11-01', '2024-11-15');


-- ==========================================================
-- 2. SEED: UNIVERSITY PROGRAMS
-- ==========================================================


INSERT INTO programs (university_id, name, degree, field_of_study, duration_semesters, tuition_fee) VALUES
-- TU Berlin (university_id = 1)
(1, 'Computer Science', 'Master of Science', 'Informatics and Data Engineering', 4, 0.00),
(1, 'Global Production Engineering', 'Master of Science', 'Engineering Management', 4, 15500.00),

-- RWTH Aachen (university_id = 2)
(2, 'Software Systems Engineering', 'Master of Science', 'Computer Science & Software Architecture', 4, 0.00),
(2, 'Automotive Engineering', 'Master of Science', 'Mechanical Engineering', 3, 0.00);


-- ==========================================================
-- 3. SEED: UNIVERSITY INTAKES
-- ==========================================================


INSERT INTO intakes (university_id, name, start_month, application_deadline) VALUES
-- TU Berlin (university_id = 1)
(1, 'Winter Semester 2026', 'October', '2026-05-31'),
(1, 'Summer Semester 2027', 'April', '2026-10-31'),

-- RWTH Aachen (university_id = 2)
(2, 'Winter Semester 2026', 'October', '2026-03-01');


-- ==========================================================
-- 4. SEED: JOBS / VACANCIES
-- ==========================================================


INSERT INTO jobs (company_id, title, description, location, job_type, posted_date, source_url) VALUES
-- Siemens (company_id = 1)
(1, 'Backend Engineering Working Student', 'Assist team in optimizing internal relational data workflows and testing Python script wrappers.', 'Munich, Germany', 'Working Student', '2026-05-20', 'https://jobs.siemens.com/vacancies/1092'),
(1, 'Automation Systems Intern', 'Full-time internship focused on supporting engineering lifecycle simulations.', 'Erlangen, Germany', 'Internship', '2026-05-22', 'https://jobs.siemens.com/vacancies/1145'),

-- SAP (company_id = 2)
(2, 'Junior Cloud Developer', 'Full-time role focused on developing and maintaining platform microservices.', 'Walldorf, Germany', 'Full-time', '2026-05-18', 'https://jobs.sap.com/vacancies/8834'),
(2, 'Data Analytics Intern', 'Part-time data extraction role helping build enterprise report dashboards.', 'Berlin, Germany', 'Internship', '2026-05-24', NULL);

COMMIT;