from queries.executor import _execute_query
from queries.generic_queries import *


def get_all_companies():
    return get_records("companies")
        

def get_company_by_id(company_id):
    return get_records("companies", filters={"company_id": company_id}, single=True)
        

def create_company(name, industry, country, website):
    
    payload = {"name":name,
               "industry":industry,
               "country":country,
               "website":website}
    
    new_row = insert_record("companies",payload)
    return new_row


def check_company_exists(company_id):
    return check_entity_exists("companies", "company_id", company_id)


def update_company(company_id, name, industry, country, website):

    payload = {"name":name,
               "industry":industry,
               "country":country,
               "website":website}
    
    updated_row = update_record("companies","company_id",company_id,payload)
    return updated_row
    

def delete_company(company_id):
    return delete_records("companies", filters={"company_id": company_id}, single=True)


def search_companies_by_name(keyword):
    return get_records("companies", search_columns=["name"], search_query=keyword, partial_match=True)


def search_companies_by_industry(keyword):
    return get_records("companies", search_columns=["industry"], search_query=keyword, partial_match=True)


def search_companies_by_country(keyword):
    return get_records("companies", search_columns=["country"], search_query=keyword, partial_match=True)


def get_companies_sorted_by_name():
    return get_records("companies", sort_by="name")


def get_companies_sorted_by_industry():
    return get_records("companies", sort_by="industry")


def get_total_companies():
    return aggregate_records("companies", "count")


def get_companies_count_by_country():
    return aggregate_records("companies", "count", group_by="country")


def get_companies_count_by_industry():
    return aggregate_records("companies", "count", group_by="industry")
        