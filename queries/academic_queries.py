from queries.executor import _execute_query
from queries.generic_queries import *


def get_all_universities():
    return get_records("universities")
        


def get_university_by_id(university_id):   
    return get_records("universities", filters={"university_id": university_id}, single=True)
        


def create_university(name, country, ranking, website):
   
    payload = {"name":name,
               "country":country,
               "ranking":ranking,
               "website":website}
    
    new_row = insert_record("universities", payload)
    return new_row
        


def check_university_exists(university_id):   
    return check_entity_exists("universities", "university_id", university_id)      


def update_university(university_id, name, country, ranking, website):
   
    payload = {"name":name,
               "country":country,
               "ranking":ranking,
               "website":website}
    
    updated_row = update_record("universities","university_id",university_id,payload)
    return updated_row
        

def delete_university(university_id):   
    return delete_records("universities", filters={"university_id": university_id})


def get_universities_by_country(country):
    return get_records("universities", filters={"country": country})


def search_universities_by_name(keyword):
    return get_records("universities", search_columns=["name"], search_query=keyword, partial_match=True)


def search_universities_by_country(keyword):
    return get_records("universities", search_columns=["country"], search_query=keyword, partial_match=True)


def get_universities_by_ranking(rank):
    
    query = '''
    select * from universities
    where ranking is not null
    and ranking < %s
    order by ranking'''
    params = (rank,)
    rows = _execute_query(query, params, "fetchall")
    if rows is None:
        rows = []

    return rows


def get_universities_between_range(min_rank,max_rank):

    query = '''
    select * from universities
    where ranking > %s
    and ranking < %s
    order by ranking
    '''
    params = (min_rank,max_rank)
    rows = _execute_query(query, params, "fetchall")
    if rows is None:
        rows = []

    return rows


def get_universities_sorted_by_name():
    return get_records("universities", sort_by="name")


def get_universities_sorted_by_ranking():
    return get_universities_sorted_by_ranking_without_NULL()


def get_total_universities():
    return aggregate_records("universities","count")


def get_top_10_universities():
    return get_universities_sorted_by_ranking_without_NULL(limit = 10)


def get_universities_count_by_country():
    return aggregate_records("universities", "count", group_by="country")


        