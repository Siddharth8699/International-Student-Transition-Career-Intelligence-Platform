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
                        6. Search Users By Name
                        7. Search Users By Country
                        8. Users Older Than Age
                        9. Users Between Age Range
                        10. Sort Users By Name
                        11. Sort Users By Date Of Birth
                        12. Total Users
                        13. Average User Age
                        14. Youngest User
                        15. Oldest User
                        16. Users Per Country

                        0. Back
                        Enter your choice: ''')

                        if choice == "0":

                            print("Going back to last Menu options..")
                            break

                        elif choice ==  "1":

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
                            row = update_user(user_id,full_name, email, country_of_origin, date_of_birth)
                            display_result(row, "User not updated. Something went wrong")

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
                            rows = get_users_between_range(min_age,max_age)
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
                        6. Search Document Type By Name
                        7. Filter By Category
                        8. Sort By Name
                        9. Total Document Types
                        10. Document Types Per Category

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

                        
                        elif choice == "6":

                            search_keyword = get_clean_name("Enter the document search keyword: ")
                            rows = search_document_types_by_name(search_keyword)
                            display_result(rows)


                        elif choice == "7":

                            category = choose_document_category()
                            rows = get_document_types_by_category(category)
                            display_result(rows)


                        elif choice == "8":

                            rows = get_document_types_sorted_by_name()
                            display_result(rows)


                        elif choice == "9":

                            row = get_total_document_types()
                            display_metric(row, "Total doument types")


                        elif choice == "10":

                            rows = get_document_types_count_by_category()
                            display_result(rows)
                    

                        

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
                        6. Search Expense Category By Name
                        7. Sort Categories By Name
                        8. Total Expense Categories
                                       
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

                        elif choice == "6":

                            search_keyword = get_clean_name("Enter the search expense category keyword: ")
                            rows = search_expense_categories_by_name(search_keyword)
                            display_result(rows)

                        elif choice == "7":

                            rows = get_expense_categories_sorted_by_name()
                            display_result(rows)
                    
                        elif choice == "8":

                            row = get_total_expense_categories()
                            display_metric(row, "Total expense category")

                        
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
                        6. Search Universities By Name
                        7. Search Universities By Country
                        8. Universities Above Ranking
                        9. Universities Between Ranking Range
                        10. Sort Universities By Name
                        11. Sort Universities By Ranking
                        12. Total Universities
                        13. Top 10 Ranked University
                        14. Universities Per Country

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
                            row = get_university_by_id(university_id)
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
                            row = get_universities_by_ranking(rank)
                            display_result(row)


                        elif choice == "9":

                            min_rank = get_integer("Enter the minimum university ranking: ")
                            max_rank = get_integer("Enter the maximum university ranking: ")
                            rows = get_universities_between_range(min_rank,max_rank)
                            display_result(rows)


                        elif choice == "10":

                            rows = get_universities_sorted_by_name()
                            display_result(rows)


                        elif choice == "11":

                            rows = get_universities_sorted_by_ranking()
                            display_result(rows)


                        elif choice == "12":

                            row = get_total_universities()
                            display_metric(row, "Total university")


                        elif choice == "13":

                            rows = get_top_10_universities()
                            display_result(rows)


                        elif choice == "14":

                            row = get_universities_count_by_country()
                            display_result(row)


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
                        6. Search Companies By Name
                        7. Search Companies By Industry
                        8. Search Companies By Country
                        9. Sort Companies By Name
                        10. Sort Companies By Industry
                        11. Total Companies
                        12. Companies Per Country
                        13. Companies Per Industry

                        0. Back
                        Enter your choice: ''')

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


                        elif choice == "6":

                            search_keyword = get_entity_name("Enter the companies name search keyword: ")
                            rows = search_companies_by_name(search_keyword)
                            display_result(rows)


                        elif choice == "7":

                            search_keyword = get_entity_name("Enter the industry name search keyword: ")
                            rows = search_companies_by_industry(search_keyword)
                            display_result(rows)


                        elif choice == "8":

                            search_keyword = get_entity_name("Enter the country name search keyword: ")
                            rows = search_companies_by_country(search_keyword)
                            display_result(rows)


                        elif choice == "9":

                            rows = get_companies_sorted_by_name()
                            display_result(rows)


                        elif choice == "10":

                            rows = get_companies_sorted_by_industry()
                            display_result(rows)


                        elif choice == "11":

                            row = get_total_companies()
                            display_metric(row, "Total company")


                        elif choice == "12":

                            row = get_companies_count_by_country()
                            display_result(row)


                        elif choice == "13":

                            row = get_companies_count_by_industry()
                            display_result(row)
                    
                            
                    except BackSignal:
                        print("\n Form input canceled. Returning to Career Menu...")
                        continue

            else:
                print("Enter a valid menu option allocation (1-5).")

        except Exception as e:
            print(f"System Error Shield Activated: {e}")


if __name__ == "__main__":
    main()