from queries.executor import _execute_query

def get_all_expense_categories():
    
    query = ''' select * from expense_categories order by category_id'''
    row = _execute_query(query, None, "fetchall")
    return row
        


def get_expense_category_by_id(category_id):
   
    query = '''
    select * from expense_categories
    where category_id = %s'''
    params = (category_id,)
    row = _execute_query(query, params)
    return row



def create_expense_category(name, description):
    
    query = '''
    insert into expense_categories(name, description)
    values(%s, %s) returning *'''
    params = (name, description)
    row = _execute_query(query, params, "fetchone", True)
    return row
        


def check_expense_category_exists(category_id):
   
    query = '''
    select 1 from expense_categories
    where category_id = %s'''
    params = (category_id,)
    row = _execute_query(query, params)
    return row is not None
        


def update_expense_category(category_id, name, description):
    
    query = '''
    update expense_categories
    set name = %s,
    description = %s
    where category_id = %s
    returning *'''
    params = (name, description, category_id)
    row = _execute_query(query, params, "fetchone", True)
    return row
        


def delete_expense_category(category_id):
    
    query = '''
    delete from expense_categories
    where category_id = %s
    returning *'''
    params = (category_id, )
    row = _execute_query(query, params, "fetchone", True)
    return row
        