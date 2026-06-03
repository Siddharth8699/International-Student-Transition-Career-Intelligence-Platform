-- ====================================================================
-- 2. SYSTEM INITIALIZATION (CORE SEED)
-- ====================================================================

INSERT INTO application_statuses (application_status_id, status_name) VALUES 
(1, 'Applied'),
(2, 'Under Review'),
(3, 'Incomplete / Missing Docs'),
(4, 'Accepted'),
(5, 'Rejected')
(6, 'Withdrawn');

-- ====================================================================
-- 3. DEVELOPMENT TESTING DATA (2 RECS EACH - LINKED TO IDs 1 & 2)
-- ====================================================================

-- Insert 2 Test University Applications
INSERT INTO university_applications (
    user_id, 
    intake_id, 
    status_id, 
    application_guidance_token, 
    application_platform, 
    platform_url, 
    notes, 
    applied_date
) VALUES 
-- 1. TU Berlin - Computer Science (Winter Intake 1) -> Under Review
(
    1, 1, 2, '1-1-20260531-1001', 
    'Uni-Assist', 'https://my.uni-assist.de/', 
    'Docs uploaded. Under processing by Uni-Assist evaluations team.', 
    CURRENT_DATE - 12
),

-- 2. TU Berlin - Computer Science (Summer Intake 2) -> Incomplete
(
    1, 2, 3, '1-2-20260531-1002', 
    'University Portal', 'https://www.tu.berlin/', 
    'Missing physical letter of motivation upload.', 
    CURRENT_DATE - 5
),

-- 3. TU Berlin - Global Production Engineering (Winter Intake 3) -> Offer Accepted
(
    1, 3, 5, '1-3-20260301-1003', 
    'Uni-Assist', 'https://my.uni-assist.de/', 
    'Received official admission letter! Enrollment fee paid.', 
    CURRENT_DATE - 60
),

-- 4. RWTH Aachen - Software Systems Engineering (Winter Intake 4) -> Stuck Bottleneck (Under Review for >50 days)
(
    1, 4, 2, '1-4-20260615-1004', 
    'University Portal', 'https://online.rwth-aachen.de/', 
    'Application submitted back in April. Status still stuck on Under Review.', 
    CURRENT_DATE - 55
),

-- 5. RWTH Aachen - Software Systems Engineering (Summer Intake 5) -> Draft / Not Submitted
(
    1, 5, 1, '1-5-20260115-1005', 
    'University Portal', 'https://online.rwth-aachen.de/', 
    'Drafting modules list description assignment details.', 
    CURRENT_DATE - 2
),

-- 6. Technical University of Munich - Informatics (Winter Intake 6) -> Rejected
(
    1, 6, 6, '1-6-20260531-1006', 
    'TUMonline Portal', 'https://campus.tum.de/', 
    'Rejected due to credit mismatch in theoretical computer science prerequisites.', 
    CURRENT_DATE - 40
),

-- 7. Technical University of Munich - Data Engineering and Analytics (Winter Intake 7) -> Interview Scheduled
(
    1, 7, 4, '1-7-20260531-1007', 
    'TUMonline Portal', 'https://campus.tum.de/', 
    'Passed preliminary assessment. Mathematical entrance interview scheduled.', 
    CURRENT_DATE - 15
),

-- 8. SRH University - International Business (Fall Intake 8) -> Offer Received (Pending Decision)
(
    1, 8, 4, '1-8-20260715-1008', 
    'University Portal', 'https://www.srh-hochschule-berlin.de/', 
    'Received conditional offer letter. Decision needed before deposit deadline.', 
    CURRENT_DATE - 8
);

-- Insert 2 Test Job Applications
INSERT INTO job_applications (user_id, job_id, status_id, application_platform, platform_url, notes, applied_date) VALUES 
(
    1, 
    1, 
    1, -- Applied
    'LinkedIn', 
    'https://www.linkedin.com/jobs/tracker/', 
    'Applied via Easy Apply. Job description saved to local reference folder.',
    '2026-05-31'
),
(
    1, 
    2, 
    2, -- Under Review
    'Workday (Company Portal)', 
    'https://wd3.myworkdayjobs.com/CompanyX', 
    'Created portal profile. Application status shows "In Review" on their candidate dashboard.',
    '2026-05-31'
);