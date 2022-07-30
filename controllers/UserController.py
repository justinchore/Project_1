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
        password_input = input()
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
        #first make sure that its in a valid format -validations
        #check for the existence of email inside database. If so, raise an exception called 'EmailAlreadyRegistered' and give user option to try again or exit to menu
        #if not, then we can set return checked_email(lowercased)
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
                
    
    def check_for_exit(self, input):
        return input == 'q' or input == '/q'
