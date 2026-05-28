from utils.logger import logger

from menus.user_menu import handle_user_management
from menus.document_menu import handle_document_management
from menus.financial_menu import handle_financial_management
from menus.academic_menu import handle_academic_management
from menus.career_menu import handle_career_management



#1
def handle_main_menu():

    while True:

        try:

            choice = input("""

            1. User Management
            2. Document Management
            3. Financial Management
            4. Academic Management
            5. Career Management
            0. Exit

            Enter your choice:

            """)

            if choice == "1":

                handle_user_management()

            elif choice == "2":

                handle_document_management()

            elif choice == "3":

                handle_financial_management()

            elif choice == "4":

                handle_academic_management()

            elif choice == "5":

                handle_career_management()

            elif choice == "0":

                print("Exiting system...")
                break

            else:

                print("Invalid choice.")

        except Exception as e:

            logger.exception(e)
            print("System Error Shield Activated.")




















