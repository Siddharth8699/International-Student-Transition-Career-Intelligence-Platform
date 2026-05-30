from utils.logger import logger

from utils.input_helpers import *
from utils.display_helpers import *

from queries.user_management.users import *
from queries.user_management.user_profiles import *

from utils.exceptions import BackSignal


# ==========================================================
# USER MANAGEMENT (MAIN CONTEXT)
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

            Enter your choice: """)

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
# FLATTENED USERS MANAGEMENT
# ==========================================================

#1.1.1
def handle_users_menu():

    while True:

        try:

            print("\n===== USERS MANAGEMENT =====")

            choice = input("""
            ======================================================
            MANAGE USERS SYSTEM
            ======================================================

            ----------(CRUD)----------

            1. View All Users
            2. View User By ID
            3. Add User
            4. Update User
            5. Delete User

            ----------(Explorer)----------

            6. Search Users By Name
            7. Search Users By Country
            8. Filter Users Older Than Age
            9. Filter Users Between Age Range
            10. Sort Users By Name
            11. Sort Users By Date Of Birth

            ----------(Reports)----------

            12. Total Users
            13. Average User Age
            14. Youngest User
            15. Oldest User
            16. Users Per Country
            0. Back

            ======================================================

            Enter your choice (1-16, or 0 to Back): """)

            if choice == "0":

                print("Returning to User Management...")
                break

            elif choice == "1":

                rows = get_all_users()
                display_result(rows)

            elif choice == "2":

                user_id = get_integer("Enter the user id: ")
                row = get_user_by_id(user_id)
                display_result(row)

            elif choice == "3":

                full_name = get_clean_name("Enter the full name: ")
                email = get_email("Enter the email: ")
                country_of_origin = get_clean_name("Enter the country of user: ")
                date_of_birth = get_date("Enter the DOB: ")

                row = create_user(full_name, email, country_of_origin, date_of_birth)
                display_result(row, "User not inserted. Something went wrong.")

            elif choice == "4":

                user_id = get_integer("Enter the user id: ", 1, check_user_exists, "User id does not exist.")
                full_name = get_clean_name("Enter the full name: ")
                email = get_email("Enter the email: ")
                country_of_origin = get_clean_name("Enter the country of user: ")
                date_of_birth = get_date("Enter the DOB: ")

                row = update_user(user_id, full_name, email, country_of_origin, date_of_birth)
                display_result(row, "User not updated. Something went wrong.")

            elif choice == "5":

                user_id = get_integer("Enter the user id: ", 1, check_user_exists, "User id does not exist.")

                if confirm_delete("Delete the user id? (y/n): "):
                    row = delete_user(user_id)
                    display_result(row, "User not deleted. Something went wrong.")
                else:
                    print("Delete cancelled.")

            elif choice == "6":

                search_name = get_clean_name("Enter the search name: ")
                rows = search_users_by_name(search_name)
                display_result(rows)

            elif choice == "7":

                search_country = get_clean_name("Enter the search country: ")
                rows = search_users_by_country(search_country)
                display_result(rows)

            elif choice == "8":

                target_age = get_integer("Enter the age in years old: ")
                rows = get_users_older_than(target_age)
                display_result(rows)

            elif choice == "9":

                min_age = get_integer("Enter the minimum age: ")
                max_age = get_integer("Enter the maximum age: ")
                rows = get_users_between_range(min_age, max_age)
                display_result(rows)

            elif choice == "10":

                rows = get_users_sorted_by_name()
                display_result(rows)

            elif choice == "11":

                rows = get_users_sorted_by_DOB()
                display_result(rows)

            elif choice == "12":

                row = get_total_users()
                display_metric(row, "total users")

            elif choice == "13":

                row = get_average_user_age()
                display_metric(row, "Average user age")

            elif choice == "14":

                row = get_youngest_user()
                display_result(row)

            elif choice == "15":

                row = get_oldest_user()
                display_result(row)

            elif choice == "16":

                rows = get_users_count_by_country()
                display_result(rows)

            else:

                print("Invalid choice.")

        except BackSignal:

            print("\nForm input canceled. Returning to Users Menu...")
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
            ======================================================
            MANAGE USER PROFILES SYSTEM
            ======================================================

            ----------(CRUD)----------

            1. View All Profiles
            2. View Profile By User ID
            3. Create Profile
            4. Update Profile
            5. Delete Profile

            ----------(Explorer)----------

            6. Search Profiles By Skill
            7. Search Profiles By Language
            8. Search Profiles By Headline
            9. View Application-Ready Profiles

            ----------(Reports)----------

            10. Profile Completion Summary
            0. Back

            ======================================================

            Enter your choice (1-10, or 0 to Back): """)

            if choice == "0":

                print("Returning to User Management...")
                break

            elif choice == "1":

                rows = get_all_user_profile()
                display_result(rows)

            elif choice == "2":

                user_id = get_integer("Enter the user_id: ", 1, check_user_exists, "User id does not exist.")
                row = get_user_profile_by_user_id(user_id)
                display_result(row)

            elif choice == "3":

                user_id = get_integer("Enter the user_id: ", 1, check_user_exists, "User id does not exist.")

                if not check_profile_exists(user_id):
                    display_profile_example()
                    headline = get_text("Enter the headline: ")
                    summary = get_text("Enter the summary: ")
                    education = get_text("Enter the education: ")
                    experience = get_text("Enter the experience: ")
                    projects = get_text("Enter the projects: ")
                    skills = get_text("Enter the skills: ")
                    languages = get_text("Enter the languages: ")
                    certificates = get_text("Enter the certificates: ")
                    resume_url = get_required_text("Enter the resume URL: ")

                    row = create_user_profile(user_id, headline, summary, education, experience, projects, skills, languages, certificates, resume_url)
                    display_result(row, "User Profile not inserted.")
                else:
                    print("Profile already exists.")

            elif choice == "4":

                user_id = get_integer("Enter the user_id: ", 1, check_user_exists, "User id does not exist.")

                if check_profile_exists(user_id):
                    display_profile_example()
                    headline = get_text("Enter the headline: ")
                    summary = get_text("Enter the summary: ")
                    education = get_text("Enter the education: ")
                    experience = get_text("Enter the experience: ")
                    projects = get_text("Enter the projects: ")
                    skills = get_text("Enter the skills: ")
                    languages = get_text("Enter the languages: ")
                    certificates = get_text("Enter the certificates: ")
                    resume_url = get_required_text("Enter the resume URL: ")

                    row = update_user_profile(user_id, headline, summary, education, experience, projects, skills, languages, certificates, resume_url)
                    display_result(row, "User Profile not updated.")
                else:
                    print("User Profile does not exist.")

            elif choice == "5":

                user_id = get_integer("Enter the user_id: ", 1, check_user_exists, "User id does not exist.")

                if check_profile_exists(user_id):
                    if confirm_delete("Delete the user profile? (y/n): "):
                        row = delete_user_profile(user_id)
                        display_result(row, "User Profile not deleted.")
                    else:
                        print("Delete cancelled.")
                else:
                    print("User Profile does not exist.")

            elif choice == "6":

                search_keyword = get_entity_name("Enter the skills search keyword: ")
                rows = search_user_profiles_by_skills(search_keyword)
                display_result(rows)

            elif choice == "7":

                search_keyword = get_entity_name("Enter the language search keyword: ")
                rows = search_user_profiles_by_languages(search_keyword)
                display_result(rows)

            elif choice == "8":

                search_keyword = get_entity_name("Enter the headline search keyword: ")
                rows = search_user_profiles_by_headline(search_keyword)
                display_result(rows)

            elif choice == "9":

                rows = application_ready_user_profile()
                display_result(rows)

            elif choice == "10":

                row = get_profile_completion_summary()
                display_metric(row)

            else:

                print("Invalid choice.")

        except BackSignal:

            print("\nForm input canceled. Returning to User Profiles Menu...")
            continue

        except Exception as e:

            logger.exception(e)

            print("System Error Shield Activated.")