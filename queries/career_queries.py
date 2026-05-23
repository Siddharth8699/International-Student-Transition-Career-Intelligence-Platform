from queries.executor import _execute_query

def get_all_companies():
    
    query = ''' select * from companies order by company_id'''
    rows = _execute_query(query, None, "fetchall")
    return rows
        


def get_company_by_id(company_id):
    
    query = '''
    select * from companies
    where company_id = %s'''
    params = (company_id,)
    row = _execute_query(query, params)
    return row
        


def create_company(name, industry, country, website):
    
    query = '''
    insert into companies(name, industry, country, website)
    values(%s, %s, %s, %s) returning *'''
    params = (name, industry, country, website)
    row = _execute_query(query, params, "fetchone", True)
    return row
        


def check_company_exists(company_id):
   
    query = '''
    select 1 from companies
    where company_id = %s'''
    params = (company_id,)
    row = _execute_query(query, params)
    return row is not None
        


def update_company(company_id, name, industry, country, website):
    
    query = '''
    update companies
    set name = %s,
    industry = %s,
    country = %s,
    website = %s
    where company_id = %s
    returning *'''
    params = (name, industry, country, website, company_id)
    row = _execute_query(query, params, "fetchone", True)
    return row
    


def delete_company(company_id):
    
    query = '''
    delete from companies
    where company_id = %s
    returning *'''
    params = (company_id, )
    row = _execute_query(query, params, "fetchone", True)
    return row
        