
from queries.document_management.document_types import *

from utils.logger import logger
from utils.input_helpers import *
from utils.display_helpers import *

from utils.exceptions import BackSignal


# ==========================================================
# DOCUMENT MANAGEMENT
# ==========================================================

#1.2
def handle_document_management():

    while True:

        try:

            print("\n===== DOCUMENT MANAGEMENT =====")

            choice = input("""

            1. Manage Document Types
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_document_types_menu()

            elif choice == "0":

                print("Returning to Main Menu...")

                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# DOCUMENT TYPES MANAGEMENT
# ==========================================================

#1.2.1
def handle_document_types_menu():

    while True:

        try:

            print("\n===== DOCUMENT TYPES MANAGEMENT =====")

            choice = input("""

            1. Core Data Management (CRUD)
            2. Data Explorer
            3. Analytics & Reports
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_document_types_crud_menu()

            elif choice == "2":

                handle_document_types_explorer_menu()

            elif choice == "3":

                handle_document_types_reports_menu()

            elif choice == "0":

                print(
                    "Returning to Document Management..."
                )

                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# DOCUMENT TYPES CRUD
# ==========================================================

#1.2.1.1
def handle_document_types_crud_menu():

    while True:

        try:

            print("\n===== DOCUMENT TYPES : CRUD =====")

            choice = input("""

            1. View All Document Types
            2. View Document Type By ID
            3. Add Document Type
            4. Update Document Type
            5. Delete Document Type
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Document Types Menu..."
                )

                break

            elif choice == "1":

                rows = get_all_document_types()

                display_result(
                    rows,
                    "No document type found."
                )

            elif choice == "2":

                document_type_id = get_integer(
                    "Enter the document type id: "
                )

                row = get_document_type_by_id(
                    document_type_id
                )

                display_result(
                    row,
                    "Document type not found."
                )

            elif choice == "3":

                name = get_clean_name(
                    "Enter the document type name: "
                )

                global_category = choose_document_category()

                description = get_text(
                    "Enter the description of document type: "
                )

                row = create_document_type(
                    name,
                    global_category,
                    description
                )

                display_result(
                    row,
                    "Document type not inserted."
                )

            elif choice == "4":

                document_type_id = get_integer(
                    "Enter the document type id: ",
                    1,
                    check_document_type_exists,
                    "Document type id does not exist."
                )

                name = get_clean_name(
                    "Enter the document type name: "
                )

                global_category = choose_document_category()

                description = get_text(
                    "Enter the description of document type: "
                )

                row = update_document_type(
                    document_type_id,
                    name,
                    global_category,
                    description
                )

                display_result(
                    row,
                    "Document type not updated."
                )

            elif choice == "5":

                document_type_id = get_integer(
                    "Enter the document type id: ",
                    1,
                    check_document_type_exists,
                    "Document type id does not exist."
                )

                if confirm_delete(
                    "Delete the document type id? (y/n): "
                ):

                    row = delete_document_type(
                        document_type_id
                    )

                    display_result(
                        row,
                        "Document type not deleted."
                    )

                else:

                    print("Delete cancelled.")

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Document Types Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# DOCUMENT TYPES EXPLORER
# ==========================================================

#1.2.1.2
def handle_document_types_explorer_menu():

    while True:

        try:

            print("\n===== DOCUMENT TYPES : EXPLORER =====")

            choice = input("""

            1. Search Document Type By Name
            2. Filter By Category
            3. Sort By Name
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Document Types Menu..."
                )

                break

            elif choice == "1":

                search_keyword = get_clean_name(
                    "Enter the document search keyword: "
                )

                rows = search_document_types_by_name(
                    search_keyword
                )

                display_result(rows)

            elif choice == "2":

                category = choose_document_category()

                rows = get_document_types_by_category(
                    category
                )

                display_result(rows)

            elif choice == "3":

                rows = get_document_types_sorted_by_name()

                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Document Types Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# DOCUMENT TYPES REPORTS
# ==========================================================

#1.2.1.3
def handle_document_types_reports_menu():

    while True:

        try:

            print("\n===== DOCUMENT TYPES : REPORTS =====")

            choice = input("""

            1. Total Document Types
            2. Document Types Per Category
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Document Types Menu..."
                )

                break

            elif choice == "1":

                row = get_total_document_types()

                display_metric(
                    row,
                    "Total document types"
                )

            elif choice == "2":

                rows = get_document_types_count_by_category()

                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Document Types Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")

