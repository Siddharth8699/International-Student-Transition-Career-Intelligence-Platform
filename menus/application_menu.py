from utils.logger import logger

from utils.input_helpers import *
from utils.display_helpers import *

from utils.exceptions import BackSignal

from queries.user_management.users import *
from queries.academic_management.intakes import *
from queries.application_management.university_application import *
from queries.application_management.application_statuses import *


def handle_application_management():
    
    while True:
        try:
            print("\n===== APPLICATION MANAGEMENT =====")
            choice = input("""
            1. Manage Application Statuses (Admin Master Catalog)
            2. Manage University Applications
            3. Manage Job Applications
            0. Back

            Enter your choice: 
            """)

            if choice == "1":
                handle_application_statuses()
            elif choice == "2":
                handle_university_applications_menu()

            elif choice == "3":
                handle_job_applications_menu()
            
            elif choice == "0":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            logger.exception(e)
            print(f"System Error Shield Activated. {e}")



def handle_application_statuses():

    while True:

        try:

            print("\n===== APPLICATION STATUSES MANAGEMENT =====")

            choice = input("""
            ======================================================
            MANAGE GLOBAL APPLICATION STATUSES (ADMIN MASTER CATALOG)
            ======================================================

            ----------(CRUD)----------

            1. View All Application status
            2. Add Application Status
            3. Update Application Status
            4. Delete Application Status

            0. Back

            ======================================================

            Enter your choice (1-4, or 0 to Back): """)

            if choice == "0":

                print("Returning to Application Management...")

                break

            elif choice == "1":

                rows = get_all_application_status()
                display_table(rows, headers=['application_status_id','status_name'])

            elif choice == "2":

                name = get_entity_name("Enter the application status name: ")
                if check_status_exists(name):
                    print(f"the status {name} already exists.")
                    continue
                row = create_application_status(name)
                display_table([row], headers=['application_status_id','status_name'])

            elif choice == "3":

                application_status_id = get_integer(
                    "Enter the application status id: ",
                    1,
                    check_application_status_exists,
                    "Application status id does not exist."
                )
                name = get_entity_name("Enter the application status name: ")
                if check_status_exists(name):
                    print(f"the status {name} already exists.")
                    continue
                row = update_application_status(application_status_id, name)
                display_table([row], headers=['application_status_id','status_name'])
                

            elif choice == "4":

                application_status_id = get_integer(
                    "Enter the application status id: ",
                    1,
                    check_application_status_exists,
                    "Application status id does not exist."
                )

                if confirm_delete("Delete the application status id? (y/n): "):
                    row = delete_application_status(application_status_id)
                    display_table([row], headers=['application_status_id','status_name'])
                else:
                    print("Delete cancelled.")


            else:

                print("Invalid choice.")

        except BackSignal:

            print("\nForm input canceled. Returning to Application statuses Menu...")

            continue

        except Exception as e:

            logger.exception(e)

            print(f"System Error Shield Activated. {e}")



def handle_university_applications_menu():

    while True:
        try:
            print("\n===== UNIVERSITY APPLICATIONS MANAGEMENT =====")
            choice = input("""
            ========================================================================
                      UNIVERSITY APPLICATIONS LOG
            ========================================================================
                           
                        [ ZONE 1: DATA MANAGEMENT ]
                           
            1. Log New Submitted Application  
            2. Update Application Record     
            3. Delete Application Log
                           
            ------------------------------------------------------------------------
                           
                        [ ZONE 2: PIPELINE TRACKER ]
                           
            4. View Interactive Tracker (Show All -> Search/Filter/Select ID)
                           
            ------------------------------------------------------------------------
                           
                        [ ZONE 3: ANALYTICS & REVENUE INSIGHTS ]
                           
            5. Core Pipeline Summary (Counts, Active vs Closed, Success Rates)
            6. Strategic Targets Overview (Top Universities, Programs, Platforms)
            7. Watchlist & Bottlenecks (Stale applications, Aging monitor)
            8. Timeline & History (Monthly submission velocity, Recent logs)

            0. Back to Main System Menu
            ========================================================================
            Enter choice (0-8): 

            Enter your choice: 
            """)

            if choice == "1":

                user_id = get_integer("Enter the user id: ", 1, check_user_exists, "User id does not exist.")
                intake_id = get_integer("Enter the intake id: ", 1, check_intake_exists, "Intake id does not exist.")
                status_id = get_integer("Enter the application status id: ", 1, check_application_status_exists, "Application status does not exist.")
                if not check_univeristy_application_uniqueness(user_id, intake_id, status_id):
                    continue
                application_guidance_token = generate_application_token(user_id, intake_id)
                target_year = get_integer("Enter the targeted year: ")
                application_platform = get_text("Enter the application platform name: ")
                platform_url = get_text("Enter the platform URL: ")
                notes = get_text("Enter additional note if any: ")
                applied_date = get_date("Enter the date of application applied: ")

                row = create_university_application(user_id, intake_id, status_id, application_guidance_token, target_year, application_platform, platform_url, notes, applied_date)
                display_result(row, "Something went wrong. Application not created.")

                
            elif choice == "2":

                university_application_id = get_integer("Enter the university application id: ", 1, check_university_application_exist, "University application does not exist.")
                status_id = get_integer("Enter the application status id: ", 1, check_application_status_exists, "Application status does not exist.")
                target_year = get_integer("Enter the targeted year: ")
                application_platform = get_text("Enter the application platform name: ")
                platform_url = get_text("Enter the platform URL: ")
                notes = get_text("Enter additional note if any: ")
                applied_Date = get_date("Enter the date of application applied: ")

                row = update_university_application(university_application_id, status_id, target_year, application_platform, platform_url, notes, applied_Date)
                display_result(row, "Something went wrong. Application not updated.")


            elif choice == "3":

                university_application_id = get_integer("Enter the university application id: ", 1, check_university_application_exist, "University application does not exist.")
                if confirm_delete("Delete the university application ? (y/n): "):
                    row = delete_university_application(university_application_id)
                    display_result(row, "Something went wrong. Application not deleted")
                else:
                    print("Delete cancelled.")
                


            elif choice == "4":

                user_id = get_integer("Enter the user id: ", 1, check_user_exists, "User id does not exist.")
                search_input = get_text("Enter the search input: ")
                rows = get_university_tracker(user_id, search_input)
                display_result(rows)


            elif choice == "5":

                row = get_university_pipeline_summary()
                display_metric(row)


            elif choice == "6":

                tables = get_strategic_target_overview()
                
                if not tables:
                    print("No records found.")
                else:
                    for table in tables:
                        print(f"\n{table['title']}")
                        # Calling your exact, unchanged display function
                        display_table(table['rows'], table['headers'])


            elif choice == "7":

                rows = get_bottleneck_application()
                display_table(rows, headers=['university_name','program_name','current_status','applied_date','elapsed_days'])


            elif choice == "8":

                rows = get_intake_milestones()
                display_table(rows, headers=['intake_name','intake_year','status_name','application_count'])
                


            elif choice == "0":
                print("Returning to Main Menu...")
                break

            else:
                print("Invalid choice.")

        except Exception as e:
            logger.exception(e)
            print(f"System Error Shield Activated. {e}")



def handle_job_applications_menu():

    while True:
        try:
            print("\n===== JOB APPLICATIONS MANAGEMENT =====")
            choice = input("""
            0. Back

            Enter your choice: 
            """)

            if choice == "1":
                pass

            elif choice == "2":
                pass

            elif choice == "0":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            logger.exception(e)
            print("System Error Shield Activated.")
