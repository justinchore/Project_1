import os
import CustomExceptions
import validations.Validations as Validations
import views.UserView as UserView
import models.UserModel as User

class UserController(object):
    def __init__(self):
        self.type = 'UserController'
        self.view = UserView.UserView()
        self.model = User.User()
        self.validations = Validations.Validations()
    
    def welcome(self):
        self.view.welcome_message()
        welcome_input = int(input())
        os.system('cls')
        match welcome_input: 
            case 1:
                self.login()
            case 2:
                self.user_create()
            case 3:
                # self.view.exit_message()
                print('Exiting...')
                return 'Exit'
                
    
    def user_login(self):
        pass

    def user_create(self):
        self.view.get_firstname()
        ###firstname validation/input
        while True:
            try:
                firstname_input = input().strip()
                if firstname_input == 'q' or firstname_input == '/q':
                    print('Exiting....')
                    return None
                special_chars_val_result = self.validations.special_chars_validation(firstname_input)
                numbers_val_result = self.validations.no_numbers_validation(firstname_input)
                
                if len(special_chars_val_result) != 0:
                    raise CustomExceptions.InvalidCharactersError(special_chars_val_result)
                if len(numbers_val_result) != 0:
                    raise CustomExceptions.InvalidNumbersError
                
            except CustomExceptions.InvalidCharactersError as ice:
                print(ice.message, end="\n\n")
            except CustomExceptions.InvalidNumbersError as ine:
                print(ine.message, end="\n\n") 
            else:   
                break
        self.view.get_lastname()
        lastname_input = input().capitalize()
        self.view.get_email()
        email_input = input()
        self.view.get_password()
        password_input = input()
        self.view.get_address()
        address_input = input()

        result = self.model.create_user(firstname_input, lastname_input, email_input, password_input, address_input)
        if result == True:
            print('Success')
        
    
        
        