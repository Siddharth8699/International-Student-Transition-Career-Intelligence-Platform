from queries.executor import _execute_query
from queries.generic_queries import *

def get_all_expense_categories():
    return get_records("expense_categories") 


def get_expense_category_by_id(category_id):
    return get_records("expense_categories", filters={"category_id": category_id}, single=True)


def create_expense_category(name, description):
    
    payload = {"name":name,
               "description":description}
    new_row = insert_record("expense_categories", payload)
    return new_row    


def check_expense_category_exists(category_id):
    return check_entity_exists("expense_categories", "category_id", category_id)    


def update_expense_category(category_id, name, description):
    
    payload = {"name":name,
               "description":description}
    
    updated_row = update_record("expense_categories", "category_id", category_id, payload)
    return updated_row  


def delete_expense_category(category_id):
    return delete_records("expense_categories", filters={"category_id": category_id}, single=True)


def search_expense_categories_by_name(keyword):
    return get_records("expense_categories", search_columns=["name"], search_query=keyword, partial_match=True)


def get_expense_categories_sorted_by_name():
    return get_records("expense_categories", sort_by="name")


def get_total_expense_categories():
    return aggregate_records("expense_categories","count")
        