import os
import sys
import logging
import controllers.UserController


# class Connection(object):
#     def __init__(self, cnx=mysql.connector.connect(user=c.user, password=c.password, host=c.host, database='test'), cursor=None) -> None:
#         self.cnx = cnx
#         self.cursor = self.cnx.cursor()
        
#     @property
#     def cnx(self):
#         return self.cnx
    
#     @property
#     def cursor(self):
#         return self.cursor
    
#     def close_cursor(self):
#         self.cursor.close()
    
#     def close_connection(self):
#         self.cnx.close
        

##Start Connection:

def main():
    logging.basicConfig(filename="BookStore.log",level=logging.DEBUG, format='%(asctime)s :: %(message)s')
    
    # os.system('cls')
    user_controller = controllers.UserController.UserController()
    while not user_controller.logged_in:
        result = user_controller.welcome()
        if result == 'Exit':
            continue
        elif result == 'Exit_Store':
            return 
        elif result == 'Logged_In':
            continue
    while user_controller.is_admin == False and user_controller.logged_in:
        print("YOU ARE LOGGED IN NOW")
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
        print("Admin WORLD!")
        result = user_controller.admin_menu()
        if result == 'Exit_Store':
            return
        elif result == 'BACK_TO_ADMIN':
            continue
        elif result == 'BACK':
            continue
        
        
if __name__ == '__main__':
    main()