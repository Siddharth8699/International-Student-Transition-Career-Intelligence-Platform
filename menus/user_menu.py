
from utils.logger import logger

from utils.input_helpers import *
from utils.display_helpers import *

from queries.user_management.users import *
from queries.user_management.user_profiles import *

from utils.exceptions import BackSignal


# ==========================================================
# USER MANAGEMENT
# ==========================================================

#1.1
def handle_user_management():

    while True:

        try:

            print("\n===== USER MANAGEMENT =====")

            choice = input("""

            1. Manage Users
            2. Manage User Profiles
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_users_menu()

            elif choice == "2":

                handle_user_profiles_menu()

            elif choice == "0":

                print("Returning to Main Menu...")
                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# USERS MANAGEMENT
# ==========================================================

#1.1.1
def handle_users_menu():

    while True:

        try:

            print("\n===== USERS MANAGEMENT =====")

            choice = input("""

            1. Core Data Management (CRUD)
            2. Data Explorer
            3. Analytics & Reports
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_users_crud_menu()

            elif choice == "2":

                handle_users_explorer_menu()

            elif choice == "3":

                handle_users_reports_menu()

            elif choice == "0":

                print("Returning to User Management...")
                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# USERS CRUD
# ==========================================================

#1.1.1.1
def handle_users_crud_menu():

    while True:

        try:

            print("\n===== USERS : CRUD =====")

            choice = input("""

            1. View All Users
            2. View User By ID
            3. Add User
            4. Update User
            5. Delete User
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print("Returning to Users Menu...")
                break

            elif choice == "1":

                rows = get_all_users()

                display_result(rows)

            elif choice == "2":

                user_id = get_integer(
                    "Enter the user id: "
                )

                row = get_user_by_id(user_id)

                display_result(row)

            elif choice == "3":

                full_name = get_clean_name(
                    "Enter the full name: "
                )

                email = get_email(
                    "Enter the email: "
                )

                country_of_origin = get_clean_name(
                    "Enter the country of user: "
                )

                date_of_birth = get_date(
                    "Enter the DOB: "
                )

                row = create_user(
                    full_name,
                    email,
                    country_of_origin,
                    date_of_birth
                )

                display_result(
                    row,
                    "User not inserted. Something went wrong."
                )

            elif choice == "4":

                user_id = get_integer(
                    "Enter the user id: ",
                    1,
                    check_user_exists,
                    "User id does not exist."
                )

                full_name = get_clean_name(
                    "Enter the full name: "
                )

                email = get_email(
                    "Enter the email: "
                )

                country_of_origin = get_clean_name(
                    "Enter the country of user: "
                )

                date_of_birth = get_date(
                    "Enter the DOB: "
                )

                row = update_user(
                    user_id,
                    full_name,
                    email,
                    country_of_origin,
                    date_of_birth
                )

                display_result(
                    row,
                    "User not updated. Something went wrong."
                )

            elif choice == "5":

                user_id = get_integer(
                    "Enter the user id: ",
                    1,
                    check_user_exists,
                    "User id does not exist."
                )

                if confirm_delete(
                    "Delete the user id? (y/n): "
                ):

                    row = delete_user(user_id)

                    display_result(
                        row,
                        "User not deleted. Something went wrong."
                    )

                else:

                    print("Delete cancelled.")

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Users Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# USERS EXPLORER
# ==========================================================

#1.1.1.2
def handle_users_explorer_menu():

    while True:

        try:

            print("\n===== USERS : EXPLORER =====")

            choice = input("""

            1. Search Users By Name
            2. Search Users By Country
            3. Filter Users Older Than Age
            4. Filter Users Between Age Range
            5. Sort Users By Name
            6. Sort Users By Date Of Birth
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print("Returning to Users Menu...")
                break

            elif choice == "1":

                search_name = get_clean_name(
                    "Enter the search name: "
                )

                rows = search_users_by_name(search_name)

                display_result(rows)

            elif choice == "2":

                search_country = get_clean_name(
                    "Enter the search country: "
                )

                rows = search_users_by_country(search_country)

                display_result(rows)

            elif choice == "3":

                target_age = get_integer(
                    "Enter the age in years old: "
                )

                rows = get_users_older_than(target_age)

                display_result(rows)

            elif choice == "4":

                min_age = get_integer(
                    "Enter the minimum age: "
                )

                max_age = get_integer(
                    "Enter the maximum age: "
                )

                rows = get_users_between_range(
                    min_age,
                    max_age
                )

                display_result(rows)

            elif choice == "5":

                rows = get_users_sorted_by_name()

                display_result(rows)

            elif choice == "6":

                rows = get_users_sorted_by_DOB()

                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Users Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# USERS REPORTS
# ==========================================================

#1.1.1.3
def handle_users_reports_menu():

    while True:

        try:

            print("\n===== USERS : REPORTS =====")

            choice = input("""

            1. Total Users
            2. Average User Age
            3. Youngest User
            4. Oldest User
            5. Users Per Country
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print("Returning to Users Menu...")
                break

            elif choice == "1":

                row = get_total_users()

                display_metric(
                    row,
                    "total users"
                )

            elif choice == "2":

                row = get_average_user_age()

                display_metric(
                    row,
                    "Average user age"
                )

            elif choice == "3":

                row = get_youngest_user()

                display_result(row)

            elif choice == "4":

                row = get_oldest_user()

                display_result(row)

            elif choice == "5":

                rows = get_users_count_by_country()

                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to Users Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# USER PROFILES MANAGEMENT
# ==========================================================

#1.1.2
def handle_user_profiles_menu():

    while True:

        try:

            print("\n===== USER PROFILES MANAGEMENT =====")

            choice = input("""

            1. Core Data Management (CRUD)
            2. Data Explorer
            3. Analytics & Reports
            0. Back

            Enter your choice:

            """)

            if choice == "1":

                handle_user_profiles_crud_menu()

            elif choice == "2":

                handle_user_profiles_explorer_menu()

            elif choice == "3":

                handle_user_profiles_reports_menu()

            elif choice == "0":

                print("Returning to User Management...")
                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# USER PROFILES CRUD
# ==========================================================

#1.1.2.1
def handle_user_profiles_crud_menu():

    while True:

        try:

            print("\n===== USER PROFILES : CRUD =====")

            choice = input("""

            1. View All Profiles
            2. View Profile By User ID
            3. Create Profile
            4. Update Profile
            5. Delete Profile
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print("Returning to User Profiles Menu...")
                break

            elif choice == "1":

                rows = get_all_user_profile()

                display_result(rows)

            elif choice == "2":

                user_id = get_integer(
                    "Enter the user_id: ",
                    1,
                    check_user_exists,
                    "User id does not exist."
                )

                row = get_user_profile_by_user_id(
                    user_id
                )

                display_result(row)

            elif choice == "3":

                user_id = get_integer(
                    "Enter the user_id: ",
                    1,
                    check_user_exists,
                    "User id does not exist."
                )

                if not check_profile_exists(user_id):

                    display_profile_example()

                    headline = get_text(
                        "Enter the headline: "
                    )

                    summary = get_text(
                        "Enter the summary: "
                    )

                    education = get_text(
                        "Enter the education: "
                    )

                    experience = get_text(
                        "Enter the experience: "
                    )

                    projects = get_text(
                        "Enter the projects: "
                    )

                    skills = get_text(
                        "Enter the skills: "
                    )

                    languages = get_text(
                        "Enter the languages: "
                    )

                    certificates = get_text(
                        "Enter the certificates: "
                    )

                    resume_url = get_required_text(
                        "Enter the resume URL: "
                    )

                    row = create_user_profile(
                        user_id,
                        headline,
                        summary,
                        education,
                        experience,
                        projects,
                        skills,
                        languages,
                        certificates,
                        resume_url
                    )

                    display_result(
                        row,
                        "User Profile not inserted."
                    )

                else:

                    print("Profile already exists.")

            elif choice == "4":

                user_id = get_integer(
                    "Enter the user_id: ",
                    1,
                    check_user_exists,
                    "User id does not exist."
                )

                if check_profile_exists(user_id):

                    display_profile_example()

                    headline = get_text(
                        "Enter the headline: "
                    )

                    summary = get_text(
                        "Enter the summary: "
                    )

                    education = get_text(
                        "Enter the education: "
                    )

                    experience = get_text(
                        "Enter the experience: "
                    )

                    projects = get_text(
                        "Enter the projects: "
                    )

                    skills = get_text(
                        "Enter the skills: "
                    )

                    languages = get_text(
                        "Enter the languages: "
                    )

                    certificates = get_text(
                        "Enter the certificates: "
                    )

                    resume_url = get_required_text(
                        "Enter the resume URL: "
                    )

                    row = update_user_profile(
                        user_id,
                        headline,
                        summary,
                        education,
                        experience,
                        projects,
                        skills,
                        languages,
                        certificates,
                        resume_url
                    )

                    display_result(
                        row,
                        "User Profile not updated."
                    )

                else:

                    print("User Profile does not exist.")

            elif choice == "5":

                user_id = get_integer(
                    "Enter the user_id: ",
                    1,
                    check_user_exists,
                    "User id does not exist."
                )

                if check_profile_exists(user_id):

                    if confirm_delete(
                        "Delete the user profile? (y/n): "
                    ):

                        row = delete_user_profile(user_id)

                        display_result(
                            row,
                            "User Profile not deleted."
                        )

                    else:

                        print("Delete cancelled.")

                else:

                    print("User Profile does not exist.")

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to User Profiles Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# USER PROFILES EXPLORER
# ==========================================================

#1.1.2.2
def handle_user_profiles_explorer_menu():

    while True:

        try:

            print("\n===== USER PROFILES : EXPLORER =====")

            choice = input("""

            1. Search Profiles By Skill
            2. Search Profiles By Language
            3. Search Profiles By Headline
            4. View Application-Ready Profiles
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to User Profiles Menu..."
                )

                break

            elif choice == "1":

                search_keyword = get_entity_name(
                    "Enter the skills search keyword: "
                )

                rows = search_user_profiles_by_skills(
                    search_keyword
                )

                display_result(rows)

            elif choice == "2":

                search_keyword = get_entity_name(
                    "Enter the language search keyword: "
                )

                rows = search_user_profiles_by_languages(
                    search_keyword
                )

                display_result(rows)

            elif choice == "3":

                search_keyword = get_entity_name(
                    "Enter the headline search keyword: "
                )

                rows = search_user_profiles_by_headline(
                    search_keyword
                )

                display_result(rows)

            elif choice == "4":

                rows = application_ready_user_profile()

                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to User Profiles Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")


# ==========================================================
# USER PROFILES REPORTS
# ==========================================================

#1.1.2.3
def handle_user_profiles_reports_menu():

    while True:

        try:

            print("\n===== USER PROFILES : REPORTS =====")

            choice = input("""

            1. Profile Completion Summary
            0. Back

            Enter your choice:

            """)

            if choice == "0":

                print(
                    "Returning to User Profiles Menu..."
                )

                break

            elif choice == "1":

                row = get_profile_completion_summary()

                display_metric(row)

            else:

                print("Invalid choice.")

        except BackSignal:

            print(
                "\nForm input canceled. Returning to User Profiles Menu..."
            )

            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")