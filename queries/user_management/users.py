from queries.executor import _execute_query
from utils.calculations import calculate_cutoff_date
from queries.generic_queries import (
    get_records,
    insert_record,
    update_record, 
    delete_records, 
    aggregate_records, 
    check_entity_exists
)

def get_all_users():
    return get_records("users")


def get_user_by_id(user_id):
    return get_records("users", filters={"user_id":user_id}, single=True)


def get_user_by_email(email):
    return get_records("users", filters={"email":email}, single=True)
    

def create_user(full_name, email, country_of_origin, date_of_birth):
    
    payload = {"full_name":full_name,
               "email":email,
               "country_of_origin":country_of_origin,
               "date_of_birth":date_of_birth}
    new_row =  insert_record("users",payload)
    return new_row


def check_user_exists(user_id):
    return check_entity_exists("users", "user_id", user_id)


def update_user(user_id, full_name, email, country_of_origin, date_of_birth):
    
    payload = {"full_name":full_name,
               "email":email,
               "country_of_origin":country_of_origin,
               "date_of_birth":date_of_birth}
    updated_row = update_record("users", "user_id", user_id, payload)
    return updated_row


def delete_user(user_id):
    return delete_records("users", filters={"user_id": user_id}, single=True)


def get_users_by_country(country):
    return get_records("users", filters={"country_of_origin", country})


def get_users_by_date_of_birth(date_of_birth):
    return get_records("users", filters={"date_of_birth", date_of_birth})


def search_users_by_name(keyword):
    return get_records("users", search_columns=["full_name"], search_query=keyword, partial_match=True)


def search_users_by_country(keyword):
    return get_records("users", search_columns=["country_of_origin"], search_query=keyword, partial_match=True)


def get_users_older_than(age_limit):

    cutoff_date = calculate_cutoff_date(age_limit)

    query = """
    SELECT *
    FROM users
    WHERE date_of_birth < %s
    ORDER BY date_of_birth ASC
    """
    params = (cutoff_date,)
    rows = _execute_query(query, params,"fetchall")

    if rows is None:
        rows = []

    return rows


def get_users_between_range(min_age,max_age):

    min_date = calculate_cutoff_date(min_age)
    max_date = calculate_cutoff_date(max_age)

    query = '''
    select * from users
    where date_of_birth > %s
    and date_of_birth < %s
    order by date_of_birth ASC
    '''
    params = (max_date,min_date)
    rows = _execute_query(query, params, "fetchall")
    if rows is None:
        rows = []

    return rows


def get_users_sorted_by_name():
    return get_records("users", sort_by="full_name")


def get_users_sorted_by_DOB():
    return get_records("users", sort_by="date_of_birth")


def get_total_users():
    return aggregate_records("users", "count")


def get_average_user_age():

    query = """
        SELECT round(AVG(
            EXTRACT(
                YEAR FROM AGE(
                    CURRENT_DATE,
                    date_of_birth
                )
            )
        ), 2) AS value
        FROM users
    """

    row = _execute_query(
        query,
        fetch="fetchone"
    )

    return row[0] if row else 0


def get_youngest_user():
    return get_records("users",sort_by="date_of_birth",sort_order="desc", single=True, limit=1)
    

def get_oldest_user():
    return get_records("users",sort_by="date_of_birth", single=True, limit=1)


def get_users_count_by_country():
    return aggregate_records("users", "count", group_by="country_of_origin")