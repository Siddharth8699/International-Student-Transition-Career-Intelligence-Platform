from db.connection import get_db_connection
from utils.logger import logger


def _execute_query(query, params=None, fetch="fetchone", commit=False):

    conn = None
    cur = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        logger.info("Executing database query.")
        cur.execute(query, params)
        logger.info("Query executed successfully.")
        
        if commit:
            conn.commit()
            logger.info("Transaction committed.")

        if fetch:
            row = getattr(cur, fetch)()
            return row
        return None
    
    except Exception as error_message:
        if commit and conn:
            conn.rollback()
            logger.error(f"Transaction rolled back. Error: {error_message}")

        print(f"something went wrong: {error_message}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            logger.info("Database connection closed.")