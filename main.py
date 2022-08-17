import os
import sys
import logging
import controllers.UserController

def main():
    logging.basicConfig(filename="BookStore.log",level=logging.INFO, format='%(asctime)s :: %(message)s')
    
    os.system('cls')
    user_controller = controllers.UserController.UserController()
    while not user_controller.logged_in:
        
        result = user_controller.welcome()
        if result == 'Exit':
            continue
        elif result == 'Exit_Store':
            return 
        elif result == 'Logged_In':
            os.system('cls')
            continue
    while user_controller.is_admin == False and user_controller.logged_in:
        # print("YOU ARE LOGGED IN NOW")
        ##Retrieve/Create Order
        ##Show Logged in user Menu
        result = user_controller.logged_in_menu()
        if result == 'Exit':
            continue
        elif result == 'Exit_Store':
            return
        else: 
            print('Invalid input. Try again')
        
        return
    while user_controller.is_admin == True and user_controller.logged_in:
        # print("Admin WORLD!")
        result = user_controller.admin_menu()
        if result == 'Exit_Store':
            return
        elif result == 'BACK_TO_ADMIN':
            continue
        elif result == 'BACK':
            continue
        
        
if __name__ == '__main__':
    main()