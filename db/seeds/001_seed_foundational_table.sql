BEGIN;

-- =======================================================================================
-- LAYER 1: MASTER REPOSITORIES
-- =======================================================================================

-- 1. USERS (Generates user_id: 1, 2, 3)
INSERT INTO users (full_name, email, country_of_origin, date_of_birth) VALUES
('Siddharth Dev', 'siddharth.dev@example.com', 'India', '2001-08-24'),
('Elena Rostova', 'elena.rostova@example.com', 'Ukraine', '2002-11-15'),
('Carlos Mendez', 'carlos.mendez@example.com', 'Mexico', '2000-03-10');

-- 2. DOCUMENT TYPES (Generates document_type_id: 1, 2, 3)
INSERT INTO document_types (name, description) VALUES
('Passport', 'Official passport identification page.'),
('Transcript', 'Official academic transcript records.'),
('Bachelor Degree', 'Undergraduate graduation certificate.'),
('Highschool Certificate', 'Higher secondary education diploma.'),
('APS Certificate', 'Academic Evaluation Center certificate.'),
('Resume', 'Professional curriculum vitae.'),
('Cover Letter', 'Tailored professional application letter.'),
('Language Proof', 'Official certificate validating language proficiency (IELTS, German, etc.).')
ON CONFLICT (name) DO NOTHING;

-- 3. EXPENSE CATEGORIES (Generates expense_category_id: 1, 2)
INSERT INTO expense_categories (name, description) VALUES
('Visa Application Fee', 'Official national embassy processing fees'),
('Blocked Account Funding', 'Required security deposit proving necessary financial resources');

-- 4. UNIVERSITIES (Generates university_id: 1 to 9)
INSERT INTO universities (name, country, university_type, ranking, website) VALUES
('TU Berlin', 'Germany', 'Public', 147, 'https://www.tu.berlin'),
('RWTH Aachen', 'Germany', 'Public', 106, 'https://www.rwth-aachen.de'),
('Technical University of Munich', 'Germany', 'Public', 28, 'https://www.tum.de'),
('LMU Munich', 'Germany', 'Public', 59, 'https://www.lmu.de'),
('Heidelberg University', 'Germany', 'Public', 84, 'https://www.uni-heidelberg.de'),
('University of Stuttgart', 'Germany', 'Public', 314, 'https://www.uni-stuttgart.de'),
('Karlsruhe Institute of Technology', 'Germany', 'Public', 119, 'https://www.kit.edu'),
('SRH University', 'Germany', 'Private', NULL, 'https://www.srh-hochschule-berlin.de'),
('IU International University', 'Germany', 'Private', NULL, 'https://www.iu.de');

-- 5. COMPANIES (Generates company_id: 1, 2)
INSERT INTO companies (name, industry, country, website) VALUES
('Siemens', 'Engineering & Technology', 'Germany', 'https://www.siemens.com'),
('SAP', 'Enterprise Software', 'Germany', 'https://www.sap.com');


COMMIT;