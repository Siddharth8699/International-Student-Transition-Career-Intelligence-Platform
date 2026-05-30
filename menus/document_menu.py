from queries.document_management.document_types import *
from queries.document_management.user_document_progress_and_application_readiness import *
from queries.user_management.users import check_user_exists

from utils.logger import logger
from utils.input_helpers import *
from utils.display_helpers import *

from utils.exceptions import BackSignal


# ==========================================================
# DOCUMENT MANAGEMENT (MAIN CONTEXT)
# ==========================================================

#1.2
def handle_document_management():

    while True:

        try:

            print("\n===== DOCUMENT MANAGEMENT =====")

            choice = input("""
            1. Manage Global Document Types (Admin Master Catalog)
            2. Manage User Document Progress & Application Readiness
            0. Back to Main Menu

            Enter your choice: """)

            if choice == "1":

                handle_document_types_menu()

            elif choice == "2":

                handle_user_document_progress_and_application_readiness_menu()
            
            elif choice == "0":

                print("Returning to Main Menu...")

                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# FLATTENED DOCUMENT TYPES MANAGEMENT WITH VISUAL SECTIONS
# ==========================================================

#1.2.1
def handle_document_types_menu():

    while True:

        try:

            print("\n===== DOCUMENT TYPES MANAGEMENT =====")

            choice = input("""
            ======================================================
            MANAGE GLOBAL DOCUMENT TYPES (ADMIN MASTER CATALOG)
            ======================================================

            ----------(CRUD)----------

            1. View All Document Types
            2. View Document Type By ID
            3. Add Document Type
            4. Update Document Type
            5. Delete Document Type

            ----------(Explorer)----------

            6. Search Document Type By Name
            7. Sort By Name

            ----------(Reports)----------

            8. Total Document Types Summary
            0. Back

            ======================================================

            Enter your choice (1-8, or 0 to Back): """)

            if choice == "0":

                print("Returning to Document Management...")

                break

            elif choice == "1":

                rows = get_all_document_types()
                display_result(rows, "No document type found.")

            elif choice == "2":

                document_type_id = get_integer("Enter the document type id: ")
                row = get_document_type_by_id(document_type_id)
                display_result(row, "Document type not found.")

            elif choice == "3":

                name = get_clean_name("Enter the document type name: ")
                description = get_text("Enter the description of document type: ")
                row = create_document_type(name, description)
                display_result(row, "Document type not inserted.")

            elif choice == "4":

                document_type_id = get_integer(
                    "Enter the document type id: ",
                    1,
                    check_document_type_exists,
                    "Document type id does not exist."
                )
                name = get_clean_name("Enter the document type name: ")
                description = get_text("Enter the description of document type: ")
                row = update_document_type(document_type_id, name, description)
                display_result(row, "Document type not updated.")

            elif choice == "5":

                document_type_id = get_integer(
                    "Enter the document type id: ",
                    1,
                    check_document_type_exists,
                    "Document type id does not exist."
                )

                if confirm_delete("Delete the document type id? (y/n): "):
                    row = delete_document_type(document_type_id)
                    display_result(row, "Document type not deleted.")
                else:
                    print("Delete cancelled.")

            elif choice == "6":

                search_keyword = get_clean_name("Enter the document search keyword: ")
                rows = search_document_types_by_name(search_keyword)
                display_result(rows)

            elif choice == "7":

                rows = get_document_types_sorted_by_name()
                display_result(rows)

            elif choice == "8":

                row = get_total_document_types()
                display_metric(row, "Total document types")

            else:

                print("Invalid choice.")

        except BackSignal:

            print("\nForm input canceled. Returning to Document Types Menu...")

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")
            

# ==========================================================
# USER DOCUMENT PROGRESS AND APPLICATION READINESS
# ==========================================================

#1.2.2
def handle_user_document_progress_and_application_readiness_menu():

    while True:

        try:

            choice = input("""

            ======================================================
            MANAGE USER DOCUMENT PROGRESS & APPLICATION READINESS
            ======================================================
                           

            ----------(CRUD)----------

            1. Add User Document Checklist Entry
            2. Update User Document Checklist Entry
            3. Delete User Document Checklist Entry
                           
            ----------(Explorer)----------
                           
            4. View a Single User's Full Checklist
            5. Filter Users by Readiness Status
            6. Sort Users by Progress
            7. Find Users Missing a Specific Document

            ----------(Reports)----------

            8. Global Application Readiness Summary (KPI Report)
            9. System Bottleneck Report
            0. Back
                           

            ======================================================
                           
            Enter your choice (1-8):

            """)

            if choice == "0":

                print(
                    "Returning to Document Management Menu..."
                )

                break

            elif choice == "1":

                user_id = get_integer("Enter the user id: ", 1, check_user_exists, "User id does not exist.")
                document_type_id = get_integer("Enter the document type id: ", 1, check_document_type_exists)
                is_ready = get_integer("Is this document ready? (1 = Yes, 0 = No): ")
                if is_ready not in (0 , 1):
                    print("Invalid input. Must be either 0 or 1.")
                    return
                
                row = create_user_document_checklist(user_id, document_type_id, bool(is_ready))
                display_result(row)

            elif choice == "2":

                id = get_integer("Enter the id: ", 1, check_user_document_checklist_exists, "Id does not exist.")
                if is_ready not in (0 , 1):
                    print("Invalid input. Must be either 0 or 1.")
                    return
                row = update_user_document_checklist(id, bool(is_ready))
                display_result(row)

            elif choice == "3":

                user_id = get_integer("Enter the User id: ", 1, check_user_exists, "User id does not exist.")
                rows = delete_user_document_checklist(user_id)
                display_result(rows)

            elif choice == "4":

                user_id = get_integer("Enter the user id: ", 1, check_user_exists, "User id does not exist.")
                rows = user_checklist_by_user_id(user_id)
                display_table(rows, headers=["Document Name", "Document Status"])

            elif choice == "5":


                print("""
                Filter Users By Readiness Status

                1. Ready for Both
                2. University Only
                3. Job Only
                4. Neither
                """)

                readiness_choice = get_integer("Select readiness status: ")
                if readiness_choice not in(1,2,3,4):
                    print("Invlid input. Enter value 1-4.")
                    return

                match readiness_choice:

                    case 1:
                        uni_ready = True
                        job_ready = True

                    case 2:
                        uni_ready = True
                        job_ready = False

                    case 3:
                        uni_ready = False
                        job_ready = True

                    case 4:
                        uni_ready = False
                        job_ready = False

                rows = get_users_by_readiness_status(uni_ready,job_ready)

                display_table(rows, headers=["User Id", "User Name"])


            elif choice =="6":

                rows = get_sorted_user_by_progress()
                display_table(rows, headers=["User ID", "Completed Documents", "Total Documents", "Progress"])


            elif choice == "7":

                document_name = choose_document_type()
                rows = get_users_by_missing_document(document_name)
                display_table(rows, headers=["User id", "Full Name"])

            elif choice == "8":

                row = get_readiness_summary()
                display_metric(row)

            elif choice == "9":

                rows = missing_document_by_users()
                display_table(rows, headers=["Document Type Id", "Document Name", "No of User Missing Dcoument"])

            else:

                print("Invalid choice.")

        except BackSignal:

            print("\nForm input canceled. Returning to Document Management Menu...")

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")