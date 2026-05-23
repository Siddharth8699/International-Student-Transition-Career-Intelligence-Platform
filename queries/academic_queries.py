from queries.executor import _execute_query

def get_all_universities():
    
    query = ''' select * from universities order by university_id'''
    rows = _execute_query(query, None, "fetchall")
    return rows
        


def get_university_by_id(university_id):
    
    query = '''
    select * from universities
    where university_id = %s'''
    params = (university_id,)
    row = _execute_query(query, params)
    return row
        


def create_university(name, country, ranking, website):
   
    query = '''
    insert into universities(name, country, ranking, website)
    values(%s, %s, %s, %s) returning *'''
    params = (name, country, ranking, website)
    row = _execute_query(query, params, "fetchone", True)
    return row
        


def check_university_exists(university_id):
    
    query = '''
    select 1 from universities
    where university_id = %s'''
    params = (university_id,)
    row = _execute_query(query, params)
    return row is not None
        


def update_university(university_id, name, country, ranking, website):
   
    query = '''
    update universities
    set name = %s,
    country = %s,
    ranking = %s,
    website = %s
    where university_id = %s
    returning *'''
    params = (name, country, ranking, website, university_id)
    row = _execute_query(query, params, "fetchone", True)
    return row
        


def delete_university(university_id):
    
    query = '''
    delete from universities
    where university_id = %s
    returning *'''
    params = (university_id, )
    row = _execute_query(query, params, "fetchone", True)
    return row
        