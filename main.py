import os
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
    os.system('cls')
    user_controller = controllers.UserController.UserController()
    while True:
        result = user_controller.welcome()
        if result == 'Exit':
            continue
        elif result == 'Exit_Store':
            return 
        elif result == 'Logged_In':
            return 
        
        










if __name__ == '__main__':
    main()