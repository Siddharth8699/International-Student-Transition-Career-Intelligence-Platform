from queries.academic_management.universities import *
from queries.academic_management.programs import *
from queries.academic_management.intakes import *

from utils.logger import logger
from utils.input_helpers import *
from utils.display_helpers import *
from utils.exceptions import BackSignal


# 1.4
def handle_academic_management():
    while True:
        try:
            print("\n===== ACADEMIC MANAGEMENT =====")
            choice = input("""
            1. Manage Universities
            2. Manage Programs
            3. Manage Intakes
            0. Back

            Enter your choice: 
            """)

            if choice == "1":
                handle_universities_menu()
            elif choice == "2":
                handle_programs_menu()
            elif choice == "3":
                handle_intakes_menu()
            elif choice == "0":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            logger.exception(e)
            print("System Error Shield Activated.")


# 1.4.1
def handle_universities_menu():
    while True:
        try:
            print("\n===== UNIVERSITIES MANAGEMENT =====")
            choice = input("""
            --- CORE DATA MANAGEMENT (CRUD) ---
            1. View All Universities
            2. View University By ID
            3. Add University
            4. Update University
            5. Delete University

            --- DATA EXPLORER ---
            6. Search Universities By Name
            7. Search Universities By Country
            8. Universities Above Ranking
            9. Universities Between Ranking Range
            10. Sort Universities By Name
            11. Sort Universities By Ranking

            --- ANALYTICS & REPORTS ---
            12. Total Universities Report
            13. Top 10 Ranked Universities Report
            14. Universities Per Country Report
            
            0. Back

            Enter your choice: 
            """)

            if choice == "0":
                print("Returning to Academic Management...")
                break

            elif choice == "1":
                rows = get_all_universities()
                display_result(rows, "No universities found.")

            elif choice == "2":
                university_id = get_integer("Enter the university id: ")
                row = get_university_by_id(university_id)
                display_result(row, "No university found.")

            elif choice == "3":
                name = get_entity_name("Enter the university name: ")
                university_type = choose_university_type()
                country = get_clean_name("Enter the university country: ")
                ranking = get_optional_integer("Enter ranking (leave blank if unknown): ")
                website = get_required_text("Enter the university website link: ")
                
                row = create_university(name, university_type, country, ranking, website)
                display_result(row, "University not inserted.")

            elif choice == "4":
                university_id = get_integer("Enter the university id: ", 1, check_university_exists, "University id does not exist.")
                name = get_entity_name("Enter the university name: ")
                university_type = choose_university_type()
                country = get_clean_name("Enter the university country: ")
                ranking = get_optional_integer("Enter the university ranking or leave blank if unknown: ")
                website = get_required_text("Enter the university website link: ")
                
                row = update_university(university_id, name, university_type, country, ranking, website)
                display_result(row, "University not updated.")

            elif choice == "5":
                university_id = get_integer("Enter the university id: ", 1, check_university_exists, "University id does not exist.")
                if confirm_delete("Delete university? (Y/N): "):
                    row = delete_university(university_id)
                    display_result(row, "University not deleted.")
                else:
                    print("Delete cancelled.")

            elif choice == "6":
                search_keyword = get_entity_name("Enter the university name search keyword: ")
                rows = search_universities_by_name(search_keyword)
                display_result(rows)

            elif choice == "7":
                search_keyword = get_entity_name("Enter the university country search keyword: ")
                rows = search_universities_by_country(search_keyword)
                display_result(rows)

            elif choice == "8":
                rank = get_integer("Enter the university ranking: ")
                rows = get_universities_by_ranking(rank)
                display_result(rows)

            elif choice == "9":
                min_rank = get_integer("Enter the minimum university ranking: ")
                max_rank = get_integer("Enter the maximum university ranking: ")
                rows = get_universities_between_range(min_rank, max_rank)
                display_result(rows)

            elif choice == "10":
                rows = get_universities_sorted_by_name()
                display_result(rows)

            elif choice == "11":
                rows = get_universities_sorted_by_ranking()
                display_result(rows)

            elif choice == "12":
                row = get_total_universities()
                display_metric(row, "Total universities")

            elif choice == "13":
                rows = get_top_10_universities()
                display_result(rows)

            elif choice == "14":
                rows = get_universities_count_by_country()
                display_result(rows)

            else:
                print("Invalid choice.")

        except BackSignal:
            print("\nForm input canceled. Returning to Universities Menu...")
            continue
        except Exception as e:
            logger.exception(e)
            print("System Error Shield Activated.")


# 1.4.2
def handle_programs_menu():
    while True:
        try:
            print("\n===== PROGRAMS MANAGEMENT =====")
            choice = input("""
            --- CORE DATA MANAGEMENT (CRUD) ---
            1. View All Programs
            2. View Program By ID
            3. Create Program
            4. Update Program
            5. Delete Program

            --- DATA EXPLORER ---
            6. Search Programs By Name
            7. Search Programs By University Name
            8. View Programs By University ID
            9. Filter Programs By Degree
            10. View Affordable Programs

            --- ANALYTICS & REPORTS ---
            11. Program Statistics Summary Report
            12. University Program Distribution Report
            
            0. Back

            Enter your choice: 
            """)

            if choice == "0":
                print("Returning to Academic Management...")
                break

            elif choice == "1":
                rows = get_all_programs()
                display_result(rows)

            elif choice == "2":
                program_id = get_integer("Enter the program id: ", 1, check_program_exists, "Program id does not exist.")
                row = get_program_by_id(program_id)
                display_result(row)

            elif choice == "3":
                university_id = get_integer("Enter the university id: ", 1, check_university_exists, "University id does not exist.")
                name = get_entity_name("Enter the program name: ")
                degree = choose_degree()

                if not check_program_uniqueness(university_id, name, degree):
                    continue

                field_of_study = get_entity_name("Enter the field of study: ")
                duration_semesters = get_integer("Enter the number of semesters: ", 1)
                tuition_fee = get_float("Enter the tuition fee: ")
                requirement_url = get_required_text("Enter the program requirement url: ")
                
                row = create_program(university_id, name, degree, field_of_study, duration_semesters, tuition_fee, requirement_url)
                display_result(row, "Program not created.")

            elif choice == "4":
                program_id = get_integer("Enter the program id: ", 1, check_program_exists, "Program id does not exist.")
                university_id = get_integer("Enter the university id: ", 1, check_university_exists, "University id does not exist.")
                name = get_entity_name("Enter the program name: ")
                degree = choose_degree()

                if not check_program_uniqueness(university_id, name, degree):
                    continue

                field_of_study = get_entity_name("Enter the field of study: ")
                duration_semesters = get_integer("Enter the number of semesters: ", 1)
                tuition_fee = get_float("Enter the tuition fee: ")
                requirement_url = get_required_text("Enter the program requirement url: ")
                
                row = update_program(program_id, name, degree, field_of_study, duration_semesters, tuition_fee, requirement_url)
                display_result(row, "Program not updated.")

            elif choice == "5":
                program_id = get_integer("Enter the program id: ", 1, check_program_exists, "Program id does not exist.")
                if confirm_delete("Delete Program? (Y/N): "):
                    row = delete_program(program_id)
                    display_result(row, "Program not deleted.")
                else:
                    print("Delete cancelled.")

            elif choice == "6":
                search_keyword = get_entity_name("Enter the program name search keyword: ")
                rows = search_programs_by_name(search_keyword)
                display_result(rows)

            elif choice == "7":
                search_keyword = get_entity_name("Enter the university name search keyword: ")
                rows = search_programs_by_university_name(search_keyword)
                display_result(rows)

            elif choice == "8":
                university_id = get_integer("Enter the university id: ", 1, check_university_exists, "University id does not exist.")
                rows = get_programs_by_university_id(university_id)
                display_result(rows)

            elif choice == "9":
                degree = choose_degree()
                rows = get_programs_by_degree(degree)
                display_result(rows)

            elif choice == "10":
                rows = get_affordable_programs()
                display_result(rows)

            elif choice == "11":
                row = get_program_statistics_summary()
                display_metric(row)

            elif choice == "12":
                rows = get_university_program_distribution()
                display_result(rows)

            else:
                print("Invalid choice.")

        except BackSignal:
            print("\nForm input canceled. Returning to Programs Menu...")
            continue
        except Exception as e:
            logger.exception(e)
            print("System Error Shield Activated.")


# 1.4.3
def handle_intakes_menu():
    while True:
        try:
            print("\n===== INTAKES MANAGEMENT =====")
            choice = input("""
            --- CORE DATA MANAGEMENT (CRUD) ---
            1. View All Intakes
            2. View Intake By ID
            3. Create Intake
            4. Update Intake
            5. Delete Intake

            --- DATA EXPLORER ---
            6. Search Intake By Name
            7. View Program Intakes
            8. View Upcoming Deadlines

            --- ANALYTICS & REPORTS ---
            9. Intake Statistics Summary Report
            10. Program Intake Distribution Report
            
            0. Back

            Enter your choice: 
            """)

            if choice == "0":
                print("Returning to Academic Management...")
                break

            elif choice == "1":
                rows = get_all_intakes()
                display_result(rows)

            elif choice == "2":
                intake_id = get_integer("Enter the intake id: ", 1, check_intake_exists, "Intake id does not exist.")
                row = get_intake_by_id(intake_id)
                display_result(row)

            elif choice == "3":
                program_id = get_integer("Enter the program id: ", 1, check_program_exists, "Program id does not exist.")
                name = choose_intake()

                if not check_intake_uniqueness(program_id, name):
                    continue

                start_month = choose_month()
                application_deadline = get_any_date("Enter the application deadline date: ")
                
                row = create_intake(program_id, name, start_month, application_deadline)
                display_result(row, "Intake not created.")

            elif choice == "4":
                intake_id = get_integer("Enter the intake id: ", 1, check_intake_exists, "Intake id does not exist.")
                program_id = get_integer("Enter the program id: ", 1, check_program_exists, "Program id does not exist.")
                name = choose_intake()

                if not check_intake_uniqueness(program_id, name):
                    continue

                start_month = choose_month()
                application_deadline = get_any_date("Enter the application deadline date: ")
                
                row = update_intake(intake_id, name, start_month, application_deadline)
                display_result(row, "Intake not updated.")

            elif choice == "5":
                intake_id = get_integer("Enter the intake id: ", 1, check_intake_exists, "Intake id does not exist.")
                if confirm_delete("Delete Intake? (Y/N): "):
                    row = delete_intake(intake_id)
                    display_result(row)
                else:
                    print("Delete cancelled.")

            elif choice == "6":
                name = choose_intake()
                rows = get_intake_by_name(name)
                display_result(rows)

            elif choice == "7":
                program_id = get_integer("Enter the program id: ", 1, check_program_exists, "Program id does not exist.")
                rows = get_intake_by_program_id(program_id)
                display_result(rows)

            elif choice == "8":
                rows = get_upcoming_deadline()
                display_result(rows)

            elif choice == "9":
                row = get_intake_statistics_summary()
                display_metric(row)

            elif choice == "10":
                rows = get_program_intake_distribution()
                display_result(rows)

            else:
                print("Invalid choice.")

        except BackSignal:
            print("\nForm input canceled. Returning to Intakes Menu...")
            continue
        except Exception as e:
            logger.exception(e)
            print("System Error Shield Activated.")