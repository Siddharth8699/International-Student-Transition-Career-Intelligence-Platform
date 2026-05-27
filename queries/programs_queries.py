from queries.executor import _execute_query
from queries.generic_queries import *

def get_all_programs():
    return get_records("programs")


def get_program_by_id(program_id):
    return get_records("programs", filters={"program_id": program_id}, single= True)


def check_program_exists(program_id):
    return check_entity_exists("programs", "program_id", program_id)


def create_program(university_id, name, degree, field_of_study, duration_semesters, tuition_fee):

    payload = {"university_id": university_id,
               "name": name,
               "degree": degree,
               "field_of_study": field_of_study,
               "duration_semesters": duration_semesters,
               "tuition_fee": tuition_fee}

    new_row = insert_record("programs", payload)
    return new_row

def update_program(program_id, name, degree, field_of_study, duration_semesters, tuition_fee):

    payload = {"name": name,
               "degree": degree,
               "field_of_study": field_of_study,
               "duration_semesters": duration_semesters,
               "tuition_fee": tuition_fee}
    
    updated_row = update_record("programs", "program_id", program_id, payload)
    return updated_row


def delete_program(program_id):
    return delete_records("programs", filters={"program_id": program_id}, single=True)


def check_program_uniqueness(university_id, name, degree):

    exists = get_records("programs", filters={"university_id": university_id, "name": name, "degree": degree}, single=True)

    if exists:
        print("Program already exists.")

        return False

    return True


def search_programs_by_name(keyword):
    return get_records("programs", search_columns=["name"], search_query=keyword, partial_match=True)


def get_programs_by_university_id(university_id):
    return get_records("programs", filters={"university_id":university_id})


def get_programs_by_degree(degree):
    return get_records("programs", filters={"degree": degree})


def get_affordable_programs():
    return get_records("programs", filters={"tuition_fee": 0.00})


def search_programs_by_university_name(keyword):

    query = """
    SELECT p.*
    FROM programs p
    JOIN universities u
    ON p.university_id = u.university_id
    WHERE u.name ILIKE %s
    ORDER BY p.name
    """
    params = (f"%{keyword}%",)
    
    return _execute_query(query, params,"fetchall")


def get_program_statistics_summary():

    query = '''SELECT
    COUNT(*) AS total_programs,
    AVG(tuition_fee) AS avg_tuition,
    AVG(duration_semesters) AS avg_duration
    FROM programs'''

    result = _execute_query(query)

    return {
        "total_programs": result[0],
        "avg_tuition": result[1],
        "avg_duration": result[2]
        }


def get_university_program_distribution():

    query = '''SELECT
    u.name, COUNT(*)
    FROM programs p
    JOIN universities uON p.university_id=u.university_id
    GROUP BY u.name
    ORDER BY COUNT(*) DESC'''

    return _execute_query(query, (), "fetchall")