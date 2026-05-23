BEGIN;

-- 1. Users
INSERT INTO users (full_name, email, country_of_origin, date_of_birth) VALUES
('Siddharth Dev', 'siddharth.dev@example.com', 'India', '2001-08-24'),
('Elena Rostova', 'elena.rostova@example.com', 'Ukraine', '2002-11-15'),
('Carlos Mendez', 'carlos.mendez@example.com', 'Mexico', '2000-03-10');

-- 2. Document Types
INSERT INTO document_types (name, global_category, description) VALUES
('Biometric Passport', 'Relocation', 'Primary international identity document'),
('APS Certificate', 'University', 'Academic evaluation center certification'),
('Motivation Letter', 'University', 'Statement of purpose for university apps');

-- 3. Expense Categories
INSERT INTO expense_categories (name, description) VALUES
('Visa Application Fee', 'Official embassy processing fees'),
('Blocked Account Funding', 'Required proof of financial resources');

-- 4. Universities
INSERT INTO universities (name, country, ranking, website) VALUES
('TU Berlin', 'Germany', 147, 'https://www.tu.berlin'),
('RWTH Aachen', 'Germany', 106, 'https://www.rwth-aachen.de');

-- 5. Companies
INSERT INTO companies (name, industry, country, website) VALUES
('Siemens', 'Engineering & Technology', 'Germany', 'https://www.siemens.com'),
('SAP', 'Enterprise Software', 'Germany', 'https://www.sap.com');

COMMIT;