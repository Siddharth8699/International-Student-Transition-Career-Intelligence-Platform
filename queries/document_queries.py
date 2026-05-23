from queries.executor import _execute_query

def get_all_document_types():
    
        query = ''' select * from document_types order by document_type_id'''
        rows =  _execute_query(query, None, "fetchall")
        return rows



def get_document_type_by_id(document_type_id):
    
        query = '''
        select * from document_types
        where document_type_id = %s'''
        params = (document_type_id,)
        row = _execute_query(query, params)
        return row
        


def create_document_type(name, global_category, description):
    
        query = '''
        insert into document_types(name, global_category, description)
        values(%s, %s , %s) returning *'''
        params = (name, global_category, description)
        row = _execute_query(query, params, "fetchone", True)
        return row


        
def check_document_type_exists(document_type_id):
    
    query = '''
    select 1 from document_types
    where document_type_id = %s'''
    params = (document_type_id,)
    row = _execute_query(query, params)
    return row is not None
        
    

def update_document_type(document_type_id, name, global_category, description):
    
    query = '''
    update document_types
    set name = %s,
    global_category = %s,
    description = %s
    where document_type_id = %s
    returning *'''
    params = (name, global_category, description, document_type_id)
    row = _execute_query(query, params, "fetchone", True)
    return row



def delete_document_type(document_type_id):
    
    query = '''
    delete from document_types
    where document_type_id = %s
    returning *'''
    params = (document_type_id, )
    row = _execute_query(query, params, "fetchone", True)
    return row