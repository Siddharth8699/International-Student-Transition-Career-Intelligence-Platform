import logging
from queries.executor import _execute_query
from utils.validation_helpers import validate_schema

# Establish explicit repository layer logging
logger = logging.getLogger("database.generic_repository")

def get_records(
    table_name,
    *,
    filters=None,
    search_columns=None,
    search_query=None,
    partial_match=False,
    sort_by=None,
    sort_order="ASC",
    limit=None,
    single=False
):
    """
    Production Generic Selector: Builds parameterized queries dynamically 
    to handle searching, precise filtering, sorting, and pagination.
    """
    validate_schema(table_name)

    if single:
        limit = 1

    query = f"SELECT * FROM {table_name}"
    conditions = []
    params = []

    # 1. Precise Whitelisted Filtering
    if filters:
        for column_name, column_value in filters.items():
            validate_schema(table_name, column_name)
            conditions.append(f"{column_name} = %s")
            params.append(column_value)

    # 2. Text Search Optimization
    if search_query:
        if not search_columns:
            raise ValueError("Developer Error: search_columns must be defined to evaluate a search_query.")
        
        search_conditions = []
        for column_name in search_columns:
            validate_schema(table_name, column_name)
            if partial_match and isinstance(search_query, str):
                search_conditions.append(f"{column_name} ILIKE %s")
                params.append(f"%{search_query}%")
            else:
                search_conditions.append(f"{column_name} = %s")
                params.append(search_query)
        if search_conditions:
            conditions.append("(" + " OR ".join(search_conditions) + ")")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    if sort_by:
        validate_schema(table_name, sort_by)
        safe_order = "DESC" if str(sort_order).upper() == "DESC" else "ASC"
        query += f" ORDER BY {sort_by} {safe_order}"

    if limit is not None:
        query += " LIMIT %s"
        params.append(limit)

    rows = _execute_query(query, tuple(params), "fetchall")
    
    if rows is None:
        rows = []

    if single:
        return rows[0] if rows else None
    return rows


def insert_record(table_name, data):
    """
    Production Generic Insert: Dynamically builds a secure INSERT statement 
    from an explicit business-layer domain payload.
    """
    if not data:
        raise ValueError("Database Operation Error: Insert data payload cannot be empty.")

    validate_schema(table_name)

    columns = []
    placeholders = []
    params = []

    for column_name, column_value in data.items():
        validate_schema(table_name, column_name)
        columns.append(column_name)
        placeholders.append("%s")
        params.append(column_value)

    query = f"""
        INSERT INTO {table_name} ({", ".join(columns)})
        VALUES ({", ".join(placeholders)})
        RETURNING *
    """

    row = _execute_query(query, tuple(params), "fetchone", commit=True)
    if row is None:
        logger.error(f"Write failure encountered on table '{table_name}'.")
        raise RuntimeError(f"Database Execution Failure: Could not write record into '{table_name}'.")
    return row


def update_record(table_name, primary_key_column, primary_key_value, updates):
    """
    Production Generic Update: Modifies specific attributes of a record dynamically
    while isolating non-modified data.
    """
    if not updates:
        logger.warning(f"Empty update payload submitted for table '{table_name}'. Execution skipped.")
        return None

    validate_schema(table_name, primary_key_column)

    set_clauses = []
    params = []

    for column_name, column_value in updates.items():
        validate_schema(table_name, column_name)
        set_clauses.append(f"{column_name} = %s")
        params.append(column_value)

    query = f"""
        UPDATE {table_name}
        SET {", ".join(set_clauses)}
        WHERE {primary_key_column} = %s
        RETURNING *
    """
    params.append(primary_key_value)

    return _execute_query(query, tuple(params), "fetchone", commit=True)


def delete_records(table_name, filters, *, single=False):
    """
    Production Generic Deletion: Performs secure row removal operations. 
    Strictly safeguards tables against accidental mass truncation.
    """
    if not filters:
        raise ValueError("Critical Guardrail: Deletion operations require explicit filter conditions.")

    validate_schema(table_name)

    query = f"DELETE FROM {table_name}"
    conditions = []
    params = []

    for column_name, column_value in filters.items():
        validate_schema(table_name, column_name)
        conditions.append(f"{column_name} = %s")
        params.append(column_value)

    query += " WHERE " + " AND ".join(conditions)
    query += " RETURNING *"

    rows = _execute_query(query, tuple(params), "fetchall", commit=True)
    
    if rows is None:
        rows = []

    if single:
        return rows[0] if rows else None
    return rows


def aggregate_records(table_name, operation, target_column=None, *, filters=None, group_by=None):
    """
    Production Generic Analytics: Runs calculations (COUNT, SUM, AVG, MAX, MIN)
    while normalizing structural variants and empty evaluation sets.
    """
    valid_operations = {"COUNT", "SUM", "AVG", "MAX", "MIN"}
    op_upper = str(operation).upper()
    if op_upper not in valid_operations:
        raise ValueError(f"Invalid operation error. Choose from: {valid_operations}")

    validate_schema(table_name)
    if target_column:
        validate_schema(table_name, target_column)
    if group_by:
        validate_schema(table_name, group_by)

    col_target = target_column if target_column else "*"
    
    if group_by:
        query = f"SELECT {group_by}, {op_upper}({col_target}) AS value FROM {table_name}"
    else:
        query = f"SELECT {op_upper}({col_target}) AS value FROM {table_name}"

    conditions = []
    params = []

    if filters:
        for column_name, column_value in filters.items():
            validate_schema(table_name, column_name)
            conditions.append(f"{column_name} = %s")
            params.append(column_value)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    if group_by:
        query += f" GROUP BY {group_by} ORDER BY value DESC"

    rows = _execute_query(query, tuple(params), "fetchall")
    
    if rows is None:
        return [] if group_by else 0

    if group_by:
        return rows
    
    if rows:
        # If it's a dictionary cursor, grab the first value out of it safely
        if isinstance(rows[0], dict):
            val = rows[0].get("value")
        else:
            val = rows[0][0] # Grab column index 0 from row 0
            
        return val if val is not None else 0
        
    return 0


def check_entity_exists(table_name, column_name, value):
    """
    Production Verification: Executes high-efficiency index checking using SELECT 1.
    """
    validate_schema(table_name, column_name)

    query = f"SELECT 1 FROM {table_name} WHERE {column_name} = %s LIMIT 1"
    params = (value,)
    row = _execute_query(query, params, "fetchone")
    
    return bool(row)


def get_universities_sorted_by_ranking_without_NULL(limit=None):

    query = """
    SELECT *
    FROM universities
    WHERE ranking IS NOT NULL
    ORDER BY ranking ASC
    """

    params = []

    if limit:
        query += " LIMIT %s"
        params.append(limit)

    rows = _execute_query(
        query,
        tuple(params),
        "fetchall"
    )

    return rows if rows else []