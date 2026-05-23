from queries.executor import _execute_query

def get_all_users():
    
    query = ''' select * from users order by user_id'''
    rows = _execute_query(query, None, "fetchall")
    return rows



def get_user_by_id(user_id):
    
    query = '''
    select * from users
    where user_id = %s'''
    params = (user_id,)
    row = _execute_query(query, params)
    return row

    
def create_user(full_name, email, country_of_origin, date_of_birth):
    
    query = '''
    insert into users(full_name, email, country_of_origin, date_of_birth)
    values(%s, %s , %s, %s) returning *'''
    params = (full_name, email, country_of_origin, date_of_birth)
    row =  _execute_query(query, params, "fetchone", True)
    return row



def check_user_exists(user_id):
    
    query = '''
    select 1 from users
    where user_id = %s'''
    params = (user_id,)
    row = _execute_query(query, params)
    return row is not None
    
    


def update_user(user_id, full_name, email, country_of_origin, date_of_birth):
    
    query = '''
    update users
    set full_name = %s,
    email = %s,
    country_of_origin = %s,
    date_of_birth = %s
    where user_id = %s
    returning *'''
    params = (full_name, email, country_of_origin, date_of_birth, user_id)
    row = _execute_query(query, params, "fetchone", True)
    return row


def delete_user(user_id):
    
    query = '''
    delete from users
    where user_id = %s
    returning *'''
    params = (user_id, )
    row = _execute_query(query, params, "fetchone", True)
    return row