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
    }

}