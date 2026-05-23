from datetime import datetime
from utils.exceptions import BackSignal
from utils.constants import *
from utils.logger import *


def _execute_abstract_input_workflow(prompt, cast_callback, validation_callback = None):
    while True:

        raw_string = input(f"{prompt} (or press 'b' to go back): " ).strip()

        if raw_string.lower() in ('b', 'back'):
            logger.info("User canceled input workflow.")
            raise BackSignal()
        
        try:
            value = cast_callback(raw_string)

        except ValueError as error_context:
            logger.warning(f"Input format validation failed: {error_context}")
            print(f"invalid format. {error_context}")
            continue

        if validation_callback:
            error_message = validation_callback(value)
            if error_message:
                logger.warning(f"Input business validation failed: {error_message}")
                print(f"validation error. {error_message}")
                continue

        return value
    

def choose_document_category():

    while True:

        print("""
        Choose category:

        1. University
        2. Career
        3. Relocation
        """)

        choice = get_integer(
            "Enter choice: "
        )

        category = DOCUMENT_CATEGORIES.get(
            str(choice)
        )

        if category:
            return category

        print("Invalid choice.")


def get_integer(prompt, min_threshold = 0, exists_db_callback=None, missing_db_err_msg=None):

    def cast_logic(raw):
        try:
            return int(raw)
        except ValueError:
            raise ValueError("Please enter a valid number")
        
    def validation_logic(value):
        if value < min_threshold:
            return (f"Value should atleast be {min_threshold}.")
        if exists_db_callback and not exists_db_callback(value):
            return missing_db_err_msg or "Reference matching ID could not be located in database."
        return None
            
    return _execute_abstract_input_workflow(prompt, cast_logic, validation_logic)


def get_float(prompt, min_threshold=0,exists_db_callback=None,missing_db_err_msg=None):

    def cast_logic(raw):
        try:
            return float(raw)
        except ValueError:
            raise ValueError("Please enter a valid number")
        
    def validation_logic(value):
        if value < min_threshold:
            return (f"Value atleast should be {min_threshold}.")
        if exists_db_callback and not exists_db_callback(value):
            return missing_db_err_msg or "Reference matching ID could not be located in database."
        return None
        
    return _execute_abstract_input_workflow(prompt, cast_logic, validation_logic)


def get_text(prompt):

    def cast_logic(raw):
        return raw
    
    return _execute_abstract_input_workflow(prompt, cast_logic)


def get_clean_name(prompt):

    def cast_logic(raw):
        if not raw:
            raise ValueError(f"Feild cannot be empty.")
        
        if not raw.replace(" ","").isalpha():
            raise ValueError(f"Input must be only letters and space.")

        return raw.title()
    
    return _execute_abstract_input_workflow(prompt,cast_logic)


def get_entity_name(prompt):

    def cast_logic(raw):
        if not raw:
            raise ValueError(f"Feild cannot be empty.")

        return raw.title()
    
    return _execute_abstract_input_workflow(prompt,cast_logic)


def get_email(prompt):

    def cast_logic(raw):
        if not raw:
            raise ValueError(f"Feild cannot be empty.")

        if "@" not in raw or "." not in raw:
            raise ValueError(f"Enter valid email.")

        return raw.lower()
    
    return _execute_abstract_input_workflow(prompt, cast_logic)




def get_date(prompt):

    def cast_logic(raw):
        if not raw:
            raise ValueError(f"Feild cannot be empty.")
        
        try:
            parsed_date = datetime.strptime(
                raw,
                "%Y-%m-%d"
            ).date()

            return parsed_date

        except ValueError:
            raise ValueError("Please use the YYYY-MM-DD format (e.g., 2026-05-20).")

    def validation_logic(parsed_date):
        if parsed_date > datetime.today().date():
            return "Future dates are unauthorized for this tracking system."
        return None
    
    return _execute_abstract_input_workflow(prompt, cast_logic, validation_logic)


def get_required_text(prompt):

    def cast_logic(raw):
        if not raw:
            raise ValueError(f"Feild cannot be empty.")
        return raw
    
    return _execute_abstract_input_workflow(prompt, cast_logic)

    

def get_optional_integer(prompt,  min_threshold=0, exists_db_callback=None, missing_db_err_msg=None):

    def cast_logic(raw):

        if not raw:
            return None

        try:
            return int(raw)

        except ValueError:
            raise ValueError("Please enter a valid number.")


    def validation_logic(value):

        if (value is not None and value < min_threshold):
            return (f"Value should be at least {min_threshold}.")

        if (value is not None
            and exists_db_callback
            and not exists_db_callback(value)):
            return (missing_db_err_msg or "Reference matching ID could not be located in database.")

        return None


    return _execute_abstract_input_workflow(prompt, cast_logic, validation_logic)


def confirm_delete(prompt):

    def cast_logic(raw):

        raw = raw.lower()

        if raw not in ("y", "n"):
            raise ValueError("Enter y or n.")

        return raw == "y"


    return _execute_abstract_input_workflow(prompt, cast_logic)