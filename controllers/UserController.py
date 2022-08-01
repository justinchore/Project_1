import os
import emoji
import logging
from sys import settrace
import CustomExceptions
import validations.Validations as Validations
import views.UserView as UserView
import models.UserModel as User
import controllers.OrderController as OrderController
import controllers.BookController as BookController

class UserController(object):
    def __init__(self):
        self.type = 'UserController'
        self.view = UserView.UserView()
        self.user_model = User.User()
        self.validations = Validations.Validations()
        self.order_controller = OrderController.OrderController()
        self.book_controller = BookController.BookController()
        self.id = None
        self.email = None
        self.name = None
        self.is_admin = None
        self.logged_in = False
        self.current_order = None
        
    ####GETTERS#####
    
    def id(self):
        return self.id
    
    def email(self):
        return self.email
    
    def name(self):
        return self.name
    
    def is_admin(self):
        return self.is_admin
    
    def logged_in(self):
        return self.logged_in
        
    ####SETTERS######    
    
    def set_id(self, id):
        self.id = id
    
    def set_email(self, email):
        self.email = email
    
    def set_name(self, name):
        self.name = name
        
    def set_logged_in(self):
        self.logged_in = not self.logged_in
        
    def set_is_admin(self, value):
        if value == 0:
            self.is_admin = False
        else:
            self.is_admin = True
        
    ######################
    
    def welcome(self):
        self.view.welcome_message()
        welcome_input = int(input())
        os.system('cls')
        match welcome_input: 
            case 1:
                result = self.user_login()
                return result
            case 2:
                result = self.user_create()
                return result
            case 3:
                # self.view.exit_message()
                print('Exiting...')
                return 'Exit_Store'
                
    
    def user_login(self):
        os.system('cls')
        ##email address
        while True:
            try:
                self.view.login_message()
                self.view.get_email()
                email_input = input().lower()
                if email_input == '/q' or email_input == 'q': 
                    return 'Exit'
                self.view.get_login_password()
                pw_input = input()
                auth_result = self.user_model.get_user_by_email(email_input)
                if auth_result == None:
                    raise CustomExceptions.EmailNotRegistered
                print("Data from db: ", auth_result)
                pw_auth_result = self.user_model.password_auth(pw_input, auth_result["password"])

                if pw_auth_result == False:
                    raise CustomExceptions.AuthenticationFailedError
            
            except CustomExceptions.EmailNotRegistered as enr:
                print(enr.message, end="\n")
            except CustomExceptions.AuthenticationFailedError as afe:
                print(afe.message, end="\n")
            else:
                self.set_id(auth_result["user_id"])
                self.set_email(auth_result["email_address"])
                self.set_name(auth_result["first_name"])
                self.set_is_admin(auth_result["is_admin"])
                self.set_logged_in()
                self.order_controller.customer_initial_order_check(self.id)
                return 'Logged_In'
                
                
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
        
        ##password validation/input
        checked_password = self.password_check()
        if checked_password == 'Exit':
            return 'Exit'
        print('Password checked: ', checked_password)
        
        ##street_address validation/input
        checked_street = self.street_check()
        if checked_street == 'Exit':
            return 'Exit'
        print('Street checked: ', checked_street)
        
        ##city validation/input
        checked_city = self.city_check()
        if checked_city == 'Exit':
            return 'Exit'
        print('City checked: ', checked_city)
        
        ##state validation/input
        checked_state = self.state_check()
        if checked_state == 'Exit':
            return 'Exit'
        print('State checked: ', checked_state)
        
        ##zipcode validation/input
        checked_zipcode = self.zipcode_check()
        if checked_zipcode == 'Exit':
            return 'Exit'
        print('Zipcode checked: ', checked_zipcode)
        
        assembled_address = f"{checked_street} {checked_city}, {checked_state} {checked_zipcode}"

        ###ASSEMBLE ADDRESS BEFORE PASSING DATA INTO MODEL#####
        result = self.user_model.create_user(checked_fname, checked_lname, checked_email, checked_password, assembled_address)
        if result == True:
            self.view.create_user_success_msg()
            return 'Exit'
    
    def logged_in_menu(self):
        self.view.login_success_msg(self.name)
        while True:
            self.view.show_logged_in_menu()
            menu_choice = input()
            if menu_choice == 'q' or menu_choice =='q':
                print('Exiting Store...')
                return 'Exit Store'
            elif menu_choice in [1, 2, 3, 4]:
                self.book_controller.book_menu(menu_choice)
            elif menu_choice == 5:
                # self.order_controller(customer_order)
                pass
            else:
                os.system('cls')
                self.view.invalid_selection()
                continue
        
                
    
    #################CREATION/LOGIN CHECK METHODS################
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
                if self.user_model.get_user_by_email(chars):
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
                self.view.get_password()
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
                hashed_password = self.user_model.hash_password(chars)
                return hashed_password
            
    def street_check(self):
        while True:
            try:
                self.view.get_street()
                chars = input()
                if self.check_for_exit(chars):
                    return 'Exit'
                street_val_result = self.validations.street_address_validation(chars)
                print(street_val_result)
                if street_val_result == None:
                    raise CustomExceptions.InvalidStreetFormat
                
            except CustomExceptions.InvalidStreetFormat as ief:
                print(ief.message, end="\n")
            else:
                return chars
    
    def city_check(self):
        while True:
            try:
                self.view.get_city()
                chars = input().strip()
                if self.check_for_exit(chars):
                    return 'Exit'
                city_val_result1 = self.validations.special_chars_validation(chars)
                city_val_result2 = self.validations.no_numbers_validation(chars)
                
                if len(city_val_result1) != 0:
                    raise CustomExceptions.InvalidCharactersError(city_val_result1)
                if len(city_val_result2) != 0:
                    raise CustomExceptions.InvalidNumbersError(city_val_result2)
            
            except CustomExceptions.InvalidCharactersError as ice:
                print(ice.message, end="")
            except CustomExceptions.InvalidNumbersError as ine:
                print(ine.message, end="")
            else:
                capitalized_city = chars.capitalize()
                return capitalized_city
                
                
    
    def state_check(self):
        while True:
            try:
                self.view.get_state()
                chars = input().strip()
                if self.check_for_exit(chars):
                    return 'Exit'
                state_val_result = self.validations.state_validation(chars)
                
                if state_val_result == None:
                    raise CustomExceptions.InvalidStateName
            
            except CustomExceptions.InvalidStateName as isn:
                print(isn.message, end="\n")
            else:
                uppered_chars = chars.upper()
                return uppered_chars
            
    
    def zipcode_check(self):
        while True:
            try:
                self.view.get_zipcode()
                chars = input().strip()
                if self.check_for_exit(chars):
                    return 'Exit'
                zipcode_val_result = self.validations.zipcode_validation(chars)
                
                if zipcode_val_result == None:
                    raise CustomExceptions.InvalidZipCode
            
            except CustomExceptions.InvalidZipCode as izc:
                print(izc.message, end="\n")
            else:
                return chars
        
    
    def check_for_exit(self, input):
        return input == 'q' or input == '/q'
