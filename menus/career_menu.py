from queries.career_management.companies import *

from utils.logger import logger

from utils.input_helpers import *
from utils.display_helpers import *

from utils.exceptions import BackSignal


# ==========================================================
# CAREER MANAGEMENT
# ==========================================================

#1.5
def handle_career_management():

    while True:

        try:

            print("\n===== CAREER MANAGEMENT =====")

            choice = input("""

            1. Manage Companies
            2. Manage Jobs
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_companies_menu()

            # elif choice == "2":

            #     handle_jobs_menu()

            elif choice == "0":

                print("Returning to Main Menu...")

                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# COMPANIES MANAGEMENT
# ==========================================================

#1.5.1
def handle_companies_menu():

    while True:

        try:

            print("\n===== COMPANIES MANAGEMENT =====")

            choice = input("""

            1. Core Data Management (CRUD)
            2. Data Explorer
            3. Analytics & Reports
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_companies_crud_menu()

            elif choice == "2":

                handle_companies_explorer_menu()

            elif choice == "3":

                handle_companies_reports_menu()

            elif choice == "0":

                print(
                    "Returning to Career Management..."
                )

                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# COMPANIES CRUD
# ==========================================================

#1.5.1.1
def handle_companies_crud_menu():

    while True:

        try:

            print("\n===== COMPANIES : CRUD =====")

            choice = input("""

            1. View All Companies
            2. View Company By ID
            3. Add Company
            4. Update Company
            5. Delete Company
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Companies Menu..."
                )

                break

            elif choice == "1":

                rows = get_all_companies()

                display_result(
                    rows,
                    "No company found."
                )

            elif choice == "2":

                company_id = get_integer(
                    "Enter the company id: "
                )

                row = get_company_by_id(
                    company_id
                )

                display_result(
                    row,
                    "Company not found."
                )

            elif choice == "3":

                name = get_entity_name(
                    "Enter the company name: "
                )

                industry = get_entity_name(
                    "Enter the company industry: "
                )

                country = get_clean_name(
                    "Enter the company country: "
                )

                website = get_required_text(
                    "Enter the company website link: "
                )

                row = create_company(
                    name,
                    industry,
                    country,
                    website
                )

                display_result(
                    row,
                    "Company not inserted."
                )

            elif choice == "4":

                company_id = get_integer(
                    "Enter the company id: ",
                    1,
                    check_company_exists,
                    "Company id does not exist."
                )

                name = get_entity_name(
                    "Enter the company name: "
                )

                industry = get_entity_name(
                    "Enter the company industry: "
                )

                country = get_clean_name(
                    "Enter the company country: "
                )

                website = get_required_text(
                    "Enter the company website link: "
                )

                row = update_company(
                    company_id,
                    name,
                    industry,
                    country,
                    website
                )

                display_result(
                    row,
                    "Company not updated."
                )

            elif choice == "5":

                company_id = get_integer(
                    "Enter the company id: ",
                    1,
                    check_company_exists,
                    "Company id does not exist."
                )

                if confirm_delete(
                    "Delete company? (Y/N): "
                ):

                    row = delete_company(
                        company_id
                    )

                    display_result(
                        row,
                        "Company not deleted."
                    )

                else:

                    print("Delete cancelled.")

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Companies Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# COMPANIES EXPLORER
# ==========================================================

#1.5.1.2
def handle_companies_explorer_menu():

    while True:

        try:

            print("\n===== COMPANIES : EXPLORER =====")

            choice = input("""

            1. Search Companies By Name
            2. Search Companies By Industry
            3. Search Companies By Country
            4. Sort Companies By Name
            5. Sort Companies By Industry
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Companies Menu..."
                )

                break

            elif choice == "1":

                search_keyword = get_entity_name(
                    "Enter the company name search keyword: "
                )

                rows = search_companies_by_name(
                    search_keyword
                )

                display_result(rows)

            elif choice == "2":

                search_keyword = get_entity_name(
                    "Enter the industry name search keyword: "
                )

                rows = search_companies_by_industry(
                    search_keyword
                )

                display_result(rows)

            elif choice == "3":

                search_keyword = get_entity_name(
                    "Enter the country name search keyword: "
                )

                rows = search_companies_by_country(
                    search_keyword
                )

                display_result(rows)

            elif choice == "4":

                rows = get_companies_sorted_by_name()

                display_result(rows)

            elif choice == "5":

                rows = get_companies_sorted_by_industry()

                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Companies Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# COMPANIES REPORTS
# ==========================================================

#1.5.1.3
def handle_companies_reports_menu():

    while True:

        try:

            print("\n===== COMPANIES : REPORTS =====")

            choice = input("""

            1. Total Companies
            2. Companies Per Country
            3. Companies Per Industry
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to Companies Menu..."
                )

                break

            elif choice == "1":

                row = get_total_companies()

                display_metric(
                    row,
                    "Total companies"
                )

            elif choice == "2":

                rows = get_companies_count_by_country()

                display_result(rows)

            elif choice == "3":

                rows = get_companies_count_by_industry()

                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Companies Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")