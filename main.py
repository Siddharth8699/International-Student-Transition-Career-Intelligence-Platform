from db.connection import get_db_connection
from utils.logger import logger

def main():
    print("🚀 Initializing International Student Transition & Career Intelligence Platform...")
    logger.info("Platform process kicked off via main.py Entry Point.")
    
    # Test our database connection layer
    conn = get_db_connection()
    
    if conn:
        print("✅ Database Connection Test: SUCCESS!")

        cur = conn.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        
        # Close the connection pipeline immediately to prevent memory leaks
        conn.close()
        logger.info("Database connection test completed and closed safely.")
    else:
        print("❌ Database Connection Test: FAILED.")

if __name__ == "__main__":
    main()