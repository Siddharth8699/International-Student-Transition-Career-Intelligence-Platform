from queries.user_queries import *
from queries.document_queries import *
from queries.financial_queries import *
from queries.academic_queries import *
from queries.career_queries import *
from utils.input_helpers import *
from utils.display_helpers import *
from utils.logger import logger

print("Main started")


def main():
    while True:
        try:
            choice = input('''
            1. User Management
            2. Document Management
            3. Financial Management
            4. Academic Management
            5. Career Management
            Enter your choice: ''')

            if choice == "1":
                while True:
                    try:
                        choice = input('''
                        1. View All Users
                        2. View User By ID
                        3. Add User
                        4. Update User
                        5. Delete User
                        0. Back
                        Enter your choice: ''')

                        if choice == "0":

                            print("Going back to last Menu options..")
                            break

                        elif choice ==  "1":

                            rows = get_all_users()
                            display_result(rows, "No users found.")

                        elif choice == "2":
                            
                                user_id = get_integer("Enter the user id: ")
                                row = get_user_by_id(user_id)
                                display_result(row, "User not found.")

                        elif choice == "3":
                            
                            full_name = get_clean_name("Enter the full name: ")
                            email = get_email("Enter the email: ")
                            country_of_origin = get_clean_name("Enter the country of user: ")
                            date_of_birth = get_date("Enter the DOB: ")
                            row = create_user(full_name, email, country_of_origin, date_of_birth)
                            display_result(row, "User not inserted. Something went wrong")

                        elif choice == "4":

                            user_id = get_integer("Enter the user id: ", 1, check_user_exists, "User id does not exist.")
                            row = check_user_exists(user_id)
                            full_name = get_clean_name("Enter the full name: ")
                            email = get_email("Enter the email: ")
                            country_of_origin = get_clean_name("Enter the country of user: ")
                            date_of_birth = get_date("Enter the DOB: ")
                            row = update_user(user_id,full_name, email, country_of_origin, date_of_birth)
                            display_result(row, "User not updated. Something went wrong")
                        

                        elif choice == "5":
                                
                            user_id = get_integer("Enter the user id: ", 1, check_user_exists, "User id does not exist.")
                            if confirm_delete("Delete the user id? (y/n): "):
                                row = delete_user(user_id)
                                display_result(row, "User not deleted. Something went wrong")
                            else:
                                print("Delete cancelled.")
                            

                    except BackSignal:
                        print("\n Form input canceled. Returning to User Menu...")
                        continue




            elif choice == "2":
                while True:
                    try:
                        choice = input('''
                        1. View All Document Types
                        2. View Document Type By ID
                        3. Add Document Type
                        4. Update Document Type
                        5. Delete Document Type
                        0. Back
                        Enter your choice: ''')

                        if choice == "0":

                            print("Going back to last Menu options..")
                            break

                        elif choice ==  "1":
                            
                            rows = get_all_document_types()
                            display_result(rows, "No document type found")

                        elif choice == "2":
                        
                            document_type_id = get_integer("Enter the document type id: ")
                            row = get_document_type_by_id(document_type_id)
                            display_result(row, "document_type not found")

                        elif choice == "3":
                                
                            name = get_clean_name("Enter the document type name: ")
                            global_category = choose_document_category()
                            description = input("Enter the description of document type: ")

                            row = create_document_type(name, global_category, description)
                            display_result(row, "document type not inserted. Something went wrong")

                        elif choice == "4":
                            
                            document_type_id = get_integer("Enter the document type id: ", 1, check_document_type_exists, "Document type id doesnt not exist.")
                            name = get_clean_name("Enter the document type  name: ")
                            global_category = choose_document_category()
                            description = get_text("Enter the description of document type: ")
                            row = update_document_type(document_type_id, name, global_category, description)
                            display_result(row, "document type not updated. Something went wrong")
                            

                        elif choice == "5":
                            
                            document_type_id = get_integer("Enter the document type id: ", 1, check_document_type_exists, "Document type id doesnt not exist.")
                            if confirm_delete("Delete the document type id? (y/n): "):
                                row = delete_document_type(document_type_id)
                                display_result(row, "document type not deleted. Something went wrong")
                            else:
                                print("Delete cancelled.")
                        

                    except BackSignal:
                        print("\n Form input canceled. Returning to Document Menu...")
                        continue


            elif choice == "3":
                while True:
                    try:
                        choice = input('''
                        1. View All Expense Categories
                        2. View Expense Category By ID
                        3. Add Expense Category
                        4. Update Expense Category
                        5. Delete Expense Category
                        0. Back
                        Enter your choice: ''')

                        if choice == "0":

                            print("Going back to last Menu options..")
                            break

                        elif choice ==  "1":

                            rows = get_all_expense_categories()
                            display_result(rows, "No expense categories found")

                        elif choice == "2":

                            category_id = get_integer("Enter the category id: ")
                            row = get_expense_category_by_id(category_id)
                            display_result(row,"category expense not found")

                        elif choice == "3":
                            
                                name = get_clean_name("Enter the category expense name: ")
                                description = get_text("Enter the description of category expense: ")
                                row = create_expense_category(name, description)
                                display_result(row, "category expense not inserted. Something went wrong")

                        elif choice == "4":
                            
                            category_id = get_integer("Enter the category expense id: ", 1, check_expense_category_exists, "Category id does not exist.")
                            name = get_clean_name("Enter the expense category name: ")
                            description = get_text("Enter the description of expense category:")
                            row = update_expense_category(category_id, name, description)
                            display_result(row, "expense category not updated. Something went wrong")

                        elif choice == "5":
                            
                            category_id = get_integer("Enter the category expense id: ", 1, check_expense_category_exists, "Category id does not exist.")
                            if confirm_delete("Delete expense category? (Y/N): "):
                                row = delete_expense_category(category_id)
                                display_result(row, "Expense categories not deleted. Something went wrong")
                            else:
                                print("Delete cancelled.")
                            
                        
                    except BackSignal:
                        print("\n Form input canceled. Returning to Financial Menu...")
                        continue


            elif choice == "4":
                while True:
                    try:
                        choice = input('''
                        1. View All Universities
                        2. View University By ID
                        3. Add University
                        4. Update University
                        5. Delete University
                        0. Back
                        Enter your choice: ''')

                        if choice == "0":

                            print("Going back to last Menu options..")
                            break

                        elif choice ==  "1":

                            rows = get_all_universities()
                            display_result(rows, "No universities found")


                        elif choice == "2":

                            university_id = get_integer("Enter the university id: ")
                            row = get_company_by_id(university_id)
                            display_result(row, "No university found")
                                


                        elif choice == "3":
                            
                            name = get_entity_name("Enter the university name: ")
                            country = get_clean_name("Enter the university country: ")
                            ranking = get_optional_integer("Enter ranking (leave blank if unknown): ")
                            website = get_required_text("Enter the university website link: ")
                            row = create_university(name, country, ranking, website)
                            display_result(row, "university not inserted. Something went wrong")


                        elif choice == "4":

                            university_id = get_integer("Enter the university id: ", 1, check_university_exists, "University id doesnt not exist.")
                            name = get_entity_name("Enter the university name: ")
                            country = get_clean_name("Enter the university country: ")
                            ranking = get_optional_integer("Enter the university ranking or leave blank if unknown: ")
                            website = get_required_text("Enter the university website link: ")
                            row = update_university(university_id, name, country, ranking, website)
                            display_result(row, "university not updated. Something went wrong")
                        

                        elif choice == "5":
                        
                            university_id = get_integer("Enter the university id: ", 1, check_university_exists, "University id doesnt not exist.")
                            if confirm_delete("Delete university? (Y/N): "):
                                row = delete_university(university_id)
                                display_result(row, "university not deleted. Something went wrong")
                            else:
                                print("Delete cancelled.")
                            

                    except BackSignal:
                        print("\n Form input canceled. Returning to Academic Menu...")
                        continue



            elif choice == "5":
                while True:
                    try:
                        choice = input('''
                        1. View All Companies
                        2. View Company By ID
                        3. Add Company
                        4. Update Company
                        5. Delete Company
                        0. Back
                        Enter yoour choice: ''')

                        if choice == "0":

                            print("Going back to last Menu options..")
                            break

                        elif choice ==  "1":

                            rows = get_all_companies()
                            display_result(rows, "No company found")


                        elif choice == "2":
                            
                            company_id = get_integer("Enter the company id: ")
                            row = get_company_by_id(company_id)
                            display_result(row, "company not found")


                        elif choice == "3":
                            
                            name = get_entity_name("Enter the company name: ")
                            industry = get_entity_name("Enter the company industry: ")
                            country = get_clean_name("Enter the company country: ")
                            website = get_required_text("Enter the companies website link: ")
                            row = create_company(name, industry, country, website)
                            display_result(row, "company not inserted. Something went wrong")


                        elif choice == "4":
                            
                            company_id = get_integer("Enter the company id: ", 1, check_company_exists, "Company id doesn not exist.")
                            name = get_entity_name("Enter the name: ")
                            industry = get_entity_name("Enter the company industry: ")
                            country = get_clean_name("Enter the company country: ")
                            website = get_required_text("Enter the companies website link: ")
                            row = update_company(company_id, name, industry, country, website)
                            display_result(row, "company not updated. Something went wrong")
                            

                        elif choice == "5":
                            
                            company_id = get_integer("Enter the company id: ", 1, check_company_exists, "Company id doesn not exist.")
                            if confirm_delete("Delete company? (Y/N) : "):
                                row = delete_company(company_id)
                                display_result(row, "company not deleted. Something went wrong")
                            else:
                                print("Delete cancelled.")
                    
                            
                    except BackSignal:
                        print("\n Form input canceled. Returning to Career Menu...")
                        continue

            else:
                print("Enter a valid menu option allocation (1-5).")

        except Exception as e:
            print(f"System Error Shield Activated: {e}")


if __name__ == "__main__":
    main()