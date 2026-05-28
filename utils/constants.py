DOCUMENT_CATEGORIES = {
    "1": "University",
    "2": "Career",
    "3": "Relocation"
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
        "global_category",
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
        "tuition_fee"
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
        "description",
        "location",
        "job_type",
        "posted_date",
        "source_url"
    }

}