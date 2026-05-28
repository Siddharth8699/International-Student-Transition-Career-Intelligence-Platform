
from queries.financial_management.expense_categories import *

from utils.logger import logger
from utils.input_helpers import *
from utils.display_helpers import *

from utils.exceptions import BackSignal


# ==========================================================
# FINANCIAL MANAGEMENT
# ==========================================================

#1.3
def handle_financial_management():

    while True:

        try:

            print("\n===== FINANCIAL MANAGEMENT =====")

            choice = input("""

            1. Manage Expense Categories
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_expense_categories_menu()

            elif choice == "0":

                print("Returning to Main Menu...")

                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# EXPENSE CATEGORIES MANAGEMENT
# ==========================================================

#1.3.1
def handle_expense_categories_menu():

    while True:

        try:

            print("\n===== EXPENSE CATEGORIES MANAGEMENT =====")

            choice = input("""

            1. Core Data Management (CRUD)
            2. Data Explorer
            3. Analytics & Reports
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_expense_categories_crud_menu()

            elif choice == "2":

                handle_expense_categories_explorer_menu()

            elif choice == "3":

                handle_expense_categories_reports_menu()

            elif choice == "0":

                print(
                    "Returning to Financial Management..."
                )

                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# EXPENSE CATEGORIES CRUD
# ==========================================================

#1.3.1.1
def handle_expense_categories_crud_menu():

    while True:

        try:

            print("\n===== EXPENSE CATEGORIES : CRUD =====")

            choice = input("""

            1. View All Expense Categories
            2. View Expense Category By ID
            3. Add Expense Category
            4. Update Expense Category
            5. Delete Expense Category
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Expense Categories Menu..."
                )

                break

            elif choice == "1":

                rows = get_all_expense_categories()

                display_result(
                    rows,
                    "No expense categories found."
                )

            elif choice == "2":

                category_id = get_integer(
                    "Enter the category id: "
                )

                row = get_expense_category_by_id(
                    category_id
                )

                display_result(
                    row,
                    "Expense category not found."
                )

            elif choice == "3":

                name = get_clean_name(
                    "Enter the expense category name: "
                )

                description = get_text(
                    "Enter the description of expense category: "
                )

                row = create_expense_category(
                    name,
                    description
                )

                display_result(
                    row,
                    "Expense category not inserted."
                )

            elif choice == "4":

                category_id = get_integer(
                    "Enter the expense category id: ",
                    1,
                    check_expense_category_exists,
                    "Category id does not exist."
                )

                name = get_clean_name(
                    "Enter the expense category name: "
                )

                description = get_text(
                    "Enter the description of expense category: "
                )

                row = update_expense_category(
                    category_id,
                    name,
                    description
                )

                display_result(
                    row,
                    "Expense category not updated."
                )

            elif choice == "5":

                category_id = get_integer(
                    "Enter the expense category id: ",
                    1,
                    check_expense_category_exists,
                    "Category id does not exist."
                )

                if confirm_delete(
                    "Delete expense category? (Y/N): "
                ):

                    row = delete_expense_category(
                        category_id
                    )

                    display_result(
                        row,
                        "Expense category not deleted."
                    )

                else:

                    print("Delete cancelled.")

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Expense Categories Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# EXPENSE CATEGORIES EXPLORER
# ==========================================================

#1.3.1.2
def handle_expense_categories_explorer_menu():

    while True:

        try:

            print("\n===== EXPENSE CATEGORIES : EXPLORER =====")

            choice = input("""

            1. Search Expense Category By Name
            2. Sort Categories By Name
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Expense Categories Menu..."
                )

                break

            elif choice == "1":

                search_keyword = get_clean_name(
                    "Enter the search expense category keyword: "
                )

                rows = search_expense_categories_by_name(
                    search_keyword
                )

                display_result(rows)

            elif choice == "2":

                rows = get_expense_categories_sorted_by_name()

                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Expense Categories Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# EXPENSE CATEGORIES REPORTS
# ==========================================================

#1.3.1.3
def handle_expense_categories_reports_menu():

    while True:

        try:

            print("\n===== EXPENSE CATEGORIES : REPORTS =====")

            choice = input("""

            1. Total Expense Categories
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Expense Categories Menu..."
                )

                break

            elif choice == "1":

                row = get_total_expense_categories()

                display_metric(
                    row,
                    "Total expense category"
                )

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Expense Categories Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")

