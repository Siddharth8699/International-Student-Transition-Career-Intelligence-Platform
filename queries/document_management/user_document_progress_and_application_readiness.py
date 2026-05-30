from queries.executor import _execute_query
from queries.generic_queries import *


def create_user_document_checklist(user_id, document_type_id, is_ready):
    
    payload = {"user_id":user_id,
               "document_type_id":document_type_id,
               "is_ready":is_ready}
    
    new_row = insert_record("user_documents_checklist", payload)
    return new_row


def  check_user_document_checklist_exists(id):
    return check_entity_exists("user_documents_checklist", "id", id)


def update_user_document_checklist(id, is_ready):
    
    payload = {"is_ready":is_ready}
    
    updated_row = update_record("user_documents_checklist", "id", id, payload)
    return updated_row


def delete_user_document_checklist(user_id): 
    return delete_records("user_documents_checklist", filters={"user_id": user_id})


def user_checklist_by_user_id(user_id):

    query = """
    select dt.name,
    case 
    when udc.is_ready = true then 'Ready'
    when udc.is_ready = false then 'Missing'
    else 'Not Started'
    end as document_status
    from document_types as dt
    left join user_documents_checklist as udc
        on dt.document_type_id = udc.document_type_id
        and udc.user_id = %s"""
    
    params = (user_id,)

    result = _execute_query(query, params, "fetchall")
    return result


def get_users_by_readiness_status(uni_ready, job_ready):

    query = """
    select urc.user_id, u.full_name  
    from user_readiness_cache as urc
    join users as u 
    on urc.user_id = u.user_id
    where ready_for_uni = %s
    and ready_for_job = %s"""

    params = (uni_ready, job_ready)

    result =  _execute_query(query, params, "fetchall")
    return result


def get_sorted_user_by_progress():

    query = '''
    select user_id, count(*) filter(where is_ready = true) as count_of_documents,
    count(*) as total_document,
    round((count(*) filter(where is_ready = true) * 100/ count(*)),2) as progress
    from user_documents_checklist
    group by user_id
    order by progress desc'''

    result = _execute_query(query, (), "fetchall")
    return result


def get_users_by_missing_document(document_type):

    query = '''
    select u.user_id, u.full_name from users as u
    join user_documents_checklist as udc
    on u.user_id = udc.user_id
    join document_types as dt
    on udc.document_type_id = dt.document_type_id
    where udc.is_ready = false
    and dt.name = %s'''

    params = (document_type,)

    result = _execute_query(query, params, "fetchall")
    return result


def get_readiness_summary():

    query = """
    SELECT
        COUNT(*) AS total_users,

        COUNT(*) FILTER (
            WHERE ready_for_uni = TRUE
        ) AS university_ready,

        COUNT(*) FILTER (
            WHERE ready_for_uni = FALSE
        ) AS university_not_ready,

        COUNT(*) FILTER (
            WHERE ready_for_job = TRUE
        ) AS job_ready,

        COUNT(*) FILTER (
            WHERE ready_for_job = FALSE
        ) AS job_not_ready

    FROM user_readiness_cache;
    """

    result = _execute_query(query)

    return  {"total_users": result[0],
             "university_ready": result[1],
             "university_not_ready": result[2],
             "job_ready": result[3],
             "job_not_ready": result[4]}


def missing_document_by_users():
 
    query = '''
    select udc.document_type_id, dt.name, count(*) filter (where is_ready = false) as no_of_users 
    from user_documents_checklist as udc
    join document_types as dt on
    udc.document_type_id = dt.document_type_id
    group by udc.document_type_id, dt.name
    order by no_of_users desc'''

    params = ()

    return _execute_query(query, params, "fetchall")
