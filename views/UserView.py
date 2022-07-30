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
    
    ######Views for getting user information for creation/login
    
    @staticmethod
    def get_firstname():
        print('**************************************************************')
        print("First name: ", end='')
    @staticmethod
    def get_lastname():
        print('**************************************************************')
        print("Last name: ", end='')
    @staticmethod
    def get_email():
        print('**************************************************************')
        print("Email: ", end='')
    @staticmethod
    def get_password():
        print('**************************************************************')
        print('Please enter a password with the following: \n - Length: 8-18 characters long\n- Special character\n - Contains a lowercase letter\n - Contains an uppercase letter\n - Contains a number\n Enter password: ', end='')
    @staticmethod
    def get_address():
        print('**************************************************************')
        print('Address: ', end='')
          