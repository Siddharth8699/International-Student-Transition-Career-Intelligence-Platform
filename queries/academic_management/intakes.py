from queries.executor import _execute_query
from queries.generic_queries import *

def get_all_intakes():
    return get_records("intakes")


def get_intake_by_id(intake_id):
    return get_records("intakes", filters={"intake_id": intake_id}, single=True)


def check_intake_exists(intake_id):
    return check_entity_exists("intakes", "intake_id", intake_id)


def create_intake(program_id, name, start_month, application_deadline):

    payload = {"program_id": program_id,
               "name": name,
               "start_month": start_month,
               "application_deadline": application_deadline}

    new_row = insert_record("intakes", payload)
    return new_row


def update_intake(intake_id, name, start_month, application_deadline):

    payload = {"name": name,
               "start_month": start_month,
               "application_deadline": application_deadline}
    
    updated_row = update_record("intakes", "intake_id", intake_id, payload)
    return updated_row


def delete_intake(intake_id):
    return delete_records("intakes", filters={"intake_id": intake_id}, single=True)


def get_intake_by_name(name):
    return get_records("intakes", filters={"name": name})


def get_intake_by_program_id(program_id):
    return get_records("intakes", filters={"program_id": program_id})


def get_upcoming_deadline():
    return get_records("intakes", sort_by="application_deadline")


def get_intake_statistics_summary():

    query = '''SELECT
    COUNT(*) AS total_intakes,
    MIN(application_deadline) AS earliest_deadline,
    MAX(application_deadline) AS latest_deadline
    FROM intakes'''

    result = _execute_query(query)
    
    return {
        "total_intakes": result[0],
        "earliest_deadline": result[1],
        "latest_deadline": result[2]
        }


def get_program_intake_distribution():

    query = '''SELECT
    p.name, COUNT(i.intake_id)
    FROM programs p
    LEFT JOIN intakes i
    ON p.program_id=i.program_id
    GROUP BY p.name
    ORDER BY COUNT(i.intake_id) DESC'''

    return _execute_query(query, (), "fetchall")


def check_intake_uniqueness(program_id, name):

    exists = get_records("intakes", filters={"program_id": program_id, "name": name}, single=True)

    if exists:
        print("Intake already exists.")

        return False

    return True
