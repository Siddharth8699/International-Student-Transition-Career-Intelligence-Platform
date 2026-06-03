from queries.generic_queries import *
from queries.executor import _execute_query

def get_all_application_status():
    return get_records("application_statuses")


def create_application_status(name):
    
    payload = {"status_name":name}
    
    new_row = insert_record("application_statuses", payload)
    return new_row


def check_status_exists(name):

    query = '''select 1 from application_statuses where status_name Ilike %s'''
    params = (name,)
    result = _execute_query(query, params)
    if result:
        return True
    
    return False
  
def check_application_status_exists(application_status_id):   
    return check_entity_exists("application_statuses", "application_status_id", application_status_id)
           

def update_application_status(application_status_id, name):
    
    payload = {"status_name":name}

    updated_row = update_record("application_statuses","application_status_id",application_status_id,payload)
    return updated_row


def delete_application_status(application_status_id): 
    return delete_records("application_statuses", filters={"application_status_id": application_status_id}, single=True)