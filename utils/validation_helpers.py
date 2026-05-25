from utils.constants import *


def validate_schema(table_name,column_name=None):

    if table_name not in QUERYABLE_SCHEMA:

        raise ValueError("Unsupported table")

    if column_name and (column_name not in QUERYABLE_SCHEMA[table_name]):

        raise ValueError("Unsupported column")