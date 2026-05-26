DOCUMENT_CATEGORIES = {
    "1": "University",
    "2": "Career",
    "3": "Relocation"
}


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
        "university_id",
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