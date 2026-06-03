DOCUMENT_TYPES = {
    "1": "Passport",
    "2": "Transcript",
    "3": "Bachelor Degree",
    "4": "Highschool Certificate",
    "5": "APS Certificate",
    "6": "Resume",
    "7": "Cover Letter",
    "8": "Language Proof"
}


DEGREE_TYPES = {
    "1": "Bachelor",
    "2": "Master",
    "3": "PhD",
    "4": "Diploma",
    "5": "Certificate",
    "6": "Foundation",
    "7": "Other"
}


UNIVERSITY_TYPES = {
    "1": "Public",
    "2": "Private",
    "3": "Other"
}


MONTHS = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


INTAKE_TYPES = {
    "1": "Winter",
    "2": "Summer",
    "3": "Spring",
    "4": "Fall"
}


JOB_TYPES = {
    "1": "Full-time",
    "2": "Part-time",
    "3": "Working Student",
    "4": "Internship",
    "5": "Contract" }


WORK_MODES = {
    "1": "Onsite",
    "2": "Hybrid",
    "3": "Remote" }


QUERYABLE_SCHEMA = {
    "users": {
        "user_id",
        "full_name",
        "email",
        "country_of_origin",
        "date_of_birth"
    },

    "document_types": {
        "document_type_id",
        "name",
        "description"
    },

    "expense_categories": {
        "category_id",
        "name",
        "description"
    },

    "universities": {
        "university_id",
        "name",
        "university_type",
        "country",
        "ranking",
        "website"
    },

    "companies": {
        "company_id",
        "name",
        "industry",
        "country",
        "website"
    },

    "user_profiles": {
        "profile_id",
        "user_id",
        "headline",
        "summary",
        "education",
        "experience",
        "projects",
        "skills",
        "languages",
        "certificates",
        "resume_url"
    },

    "programs": {
        "program_id",
        "university_id",
        "name",
        "degree",
        "field_of_study",
        "duration_semesters",
        "tuition_fee",
        "requirement_url"
    },

    "intakes": {
        "intake_id",
        "program_id",
        "name",
        "start_month",
        "application_deadline"
    },

    "jobs": {
        "job_id",
        "company_id",
        "title",
        "location",
        "description",
        "work_mode",
        "job_type",
        "salary_min",
        "salary_max",
        "currency",
        "posted_date",
        "application_deadline",
        "source_url"
    },

    "user_documents_checklist": {
        "id",
        "user_id",
        "document_type_id",
        "is_ready"
    },

    "user_readiness_cache": {
        "user_id",
        "has_passport",
        "has_transcripts",
        "has_bachelors_degree",
        "has_highschool_cert",
        "has_aps_certificate",
        "has_resume",
        "has_cover_letter",
        "has_language_proof",
        "ready_for_uni",
        "ready_for_job"
    },

    "application_statuses": {
        "application_status_id",
        "status_name"
    },

    "university_applications": {
        "university_application_id",
        "user_id",
        "intake_id",
        "status_id",
        "application_guidance_token",
        "target_year",
        "application_platform",
        "platform_url",
        "notes",
        "applied_date"
    },

    "university_application_history": {
        "university_application_history_id",
        "university_application_id",
        "status_id",
        "notes",
        "changed_at"
    }
}