from queries.executor import _execute_query
from queries.generic_queries import *

def get_all_user_profile():
    return get_records("user_profiles")


def get_user_profile_by_user_id(user_id):
    return get_records("user_profiles", filters={"user_id": user_id}, single=True) 


def check_profile_exists(user_id):
    return check_entity_exists("user_profiles", "user_id", user_id)


def create_user_profile(user_id, headline, summary, education, experience, projects, skills, languages, certificates, resume_url):

    payload = {"user_id": user_id,
               "headline": headline,
               "summary": summary,
               "education": education,
               "experience": experience,
               "projects": projects,
               "skills": skills,
               "languages": languages,
               "certificates": certificates,
               "resume_url": resume_url}

    new_row = insert_record("user_profiles", payload)
    return new_row


def update_user_profile(user_id, headline, summary, education, experience, projects, skills, languages, certificates, resume_url):

    payload = {"headline": headline,
               "summary": summary,
               "education": education,
               "experience": experience,
               "projects": projects,
               "skills": skills,
               "languages": languages,
               "certificates": certificates,
               "resume_url": resume_url}
    
    updated_row = update_record("user_profiles", "user_id", user_id, payload)
    return updated_row


def delete_user_profile(user_id):
    return delete_records("user_profiles", filters={"user_id": user_id}, single=True)


def search_user_profiles_by_skills(keyword):
    return get_records("user_profiles", search_columns=["skills"], search_query=keyword, partial_match=True)


def search_user_profiles_by_languages(keyword):
    return get_records("user_profiles", search_columns=["languages"], search_query=keyword, partial_match=True)


def search_user_profiles_by_headline(keyword):
    return get_records("user_profiles", search_columns=["headline"], search_query=keyword, partial_match=True)


def get_profile_completion_summary():

    query = """
    SELECT
    COUNT(*) AS total_profiles,
    COUNT(education) AS profiles_with_education,
    COUNT(experience) AS profiles_with_experience,
    COUNT(projects) AS profiles_with_projects
    FROM user_profiles
    """

    result = _execute_query(query)
    return {
        "total_profiles": result[0],
        "profiles_with_education": result[1],
        "profiles_with_experience": result[2],
        "profiles_with_projects": result[3]
    }


def application_ready_user_profile():

    query = '''
    select * 
    from user_profiles
    where education is not null
    and experience is not null
    and projects is not null
    and certificates is not  null
    '''

    return _execute_query(query, (), "fetchall")


def display_profile_example():

    print("""
    Example Input:

    Education: B.Tech CSE, High School,so on....

    Experience: Backend Intern, Freelance Developer, so on..

    Projects: Career Tracker, Student Dashboard, so on..

    Skills: Python, SQL, PostgreSQL, so on..

    Languages: English C1, German A2, so on..

    Certificates: Goethe A2, AWS CCP, so on..
    """)



