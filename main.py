import mysql.connector
import mysql_config as c

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



class UserModel(object):
    def __init__(self, connection) -> None:
        self.connection = connection
        

class UserView(object):
    @staticmethod
    def welcome_message():
        print('//////////////////////////////////////////////////////////////')
        print("Welcome to SOMETHING Book Store!")
        print('//////////////////////////////////////////////////////////////')
        print('Please select an option:')
        print('1) Log in to your account')
        print('2) Create an account')
        print('3) Exit store')
    
    def login_message():
        print

class UserController(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def welcome(self):
        self.view.welcome_message()
        welcome_input = input()
        if welcome_input..
        
        
    
        
        

    
        

##Start Connection:

cnx = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database='test')
cursor = cnx.cursor()
cursor.close()
cnx.close()
user_view = UserView()

def main():
    while True:
        #welcome message()
        
        break










if __name__ == '__main__':
    main()