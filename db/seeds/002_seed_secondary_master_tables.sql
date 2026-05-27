BEGIN;

-- ==========================================================
-- 1. SEED: USER PORTFOLIO
-- ==========================================================


INSERT INTO user_profiles (user_id, headline, summary, education, experience, projects, skills, languages, certificates, resume_url) VALUES
--user_id = 1
(1, 'Backend Engineering Student', 'Preparing for international education and backend opportunities.', 'B.Tech Computer Science', 'Junior Backend Developer', 'International Student Transition Platform, Portfolio CLI System', 'Python, PostgreSQL, SQL, Git', 'English C1, German A2', 'Goethe A2', 'https://resume.example.com/siddharth'),

--user_id = 2
(2, 'Data & Automation Enthusiast', 'Interested in analytics and automation workflows.', 'Bachelor of Information Systems', NULL, 'Automated Portfolio Tracker', 'Python, SQLite, JSON, Pandas', 'English B2, Ukrainian Native', NULL, 'https://resume.example.com/elena'),

--user_id = 3
(3, 'Cloud & Backend Engineering Candidate', 'Building cloud and backend capabilities.', 'Bachelor of Software Engineering', NULL, 'Cloud Deployment Sandbox', 'AWS, Python, Security', 'Spanish Native, English B2', 'AWS Certified Cloud Practitioner', 'https://resume.example.com/carlos');



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


INSERT INTO intakes (program_id, name, start_month, application_deadline) VALUES

-- Program 1
(1, 'Winter', 'October', '2026-05-31'),
(1, 'Summer', 'April', '2026-10-31'),

-- Program 2
(2, 'Winter', 'October', '2026-03-01'),

-- Program 3
(3, 'Winter', 'September', '2026-06-15'),
(3, 'Summer', 'March', '2026-01-15');


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