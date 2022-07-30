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
                return 'Exit Store'
                
    
    def user_login(self):
        pass
            

    def user_create(self):
        os.system('cls')
        ##firstname validation/input
        self.view.get_firstname()
        checked_fname = self.name_check()
        if checked_fname == 'Exit': 
            return 'Exit'
        print('First name checked and capitalized: ', checked_fname)
        
        ##lastname validation/input
        self.view.get_lastname()
        checked_lname = self.name_check()
        if checked_fname == 'Exit': 
            return 'Exit'
        print('Last name checked and capitalized: ', checked_lname)
        
        ##email validation/input
        self.view.get_email()
        checked_email = self.email_check()
        if checked_email == 'Exit':
            return 'Exit'
        print('Email checked: ', checked_email)
        
        ##passord validation/input
        self.view.get_password()
        checked_password = self.password_check()
        if checked_password == 'Exit':
            return 'Exit'
        print('Password checked: ', checked_password)
        
        
        self.view.get_address()
        address_input = input()

        result = self.model.create_user(checked_fname, checked_lname, checked_email, password_input, address_input)
        if result == True:
            print('Success')
    

    def name_check(self):
        while True:
            try: 
                chars = input().strip().lower()
                
                if self.check_for_exit(chars):
                    return 'Exit'
                                    
                special_chars_val_result = self.validations.special_chars_validation(chars)
                numbers_val_result = self.validations.no_numbers_validation(chars)
                        
                if len(special_chars_val_result) != 0:
                    raise CustomExceptions.InvalidCharactersError(special_chars_val_result)
                if len(numbers_val_result) != 0:
                    raise CustomExceptions.InvalidNumbersError(numbers_val_result)
            except CustomExceptions.InvalidCharactersError as ice:
                print(ice.message, end="")
            except CustomExceptions.InvalidNumbersError as ine:
                print(ine.message, end="") 
            else:   
                capitalized_name = chars.capitalize()
                return capitalized_name
            
    def email_check(self):
        while True:
            try:
                chars = input().strip().lower()
                if self.check_for_exit(chars):
                    return 'Exit'
                email_format_val_result = self.validations.email_format_validation(chars)
                
                if email_format_val_result == None:
                    raise CustomExceptions.InvalidEmailFormatError
                if self.model.get_user_by_email(chars):
                    raise CustomExceptions.DuplicateEmailError
                
            except CustomExceptions.InvalidEmailFormatError as ief:
                print(ief.message, end="")
            except CustomExceptions.DuplicateEmailError as dee:
                print(dee.message, end="\n\n\n")
                return 'Exit'
            else:
                return chars
    
    def password_check(self):
        while True:
            try: 
                chars = input()
                if self.check_for_exit(chars):
                    return 'Exit'
                password_format_val_result = self.validations.pw_format_validation(chars)
                
                if password_format_val_result == None:
                    raise CustomExceptions.InvalidPasswordError
            
            except CustomExceptions.InvalidPasswordError as ipe:
                print(ipe.message, end="\n")
            else:
                #return hashed_password
                hashed_password = self.model.hash_password(chars)
                return hashed_password

    
    def check_for_exit(self, input):
        return input == 'q' or input == '/q'
