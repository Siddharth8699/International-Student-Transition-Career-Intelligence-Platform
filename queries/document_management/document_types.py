from queries.executor import _execute_query
from queries.generic_queries import *


def get_all_document_types():
    return get_records("document_types")



def get_document_type_by_id(document_type_id):   
    return get_records("document_types", filters={"document_type_id": document_type_id}, single=True)
        


def create_document_type(name, description):
    
    payload = {"name":name,
               "description":description}
    
    new_row = insert_record("document_types", payload)
    return new_row

  
def check_document_type_exists(document_type_id):   
    return check_entity_exists("document_types", "document_type_id", document_type_id)
           

def update_document_type(document_type_id, name, description):
    
    payload = {"name":name,
               "description":description}
    
    updated_row = update_record("document_types","document_type_id",document_type_id,payload)
    return updated_row


def delete_document_type(document_type_id): 
    return delete_records("document_types", filters={"document_type_id": document_type_id}, single=True)


def search_document_types_by_name(keyword):
    return get_records("document_types", search_columns=["name"], search_query=keyword, partial_match=True)


def get_document_types_sorted_by_name():
    return get_records("document_types", sort_by="name")


def get_total_document_types():
    return aggregate_records("document_types","count")

