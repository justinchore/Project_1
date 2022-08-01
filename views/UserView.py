import emoji
import os

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
    def login_message():
        print(emoji.emojize(':boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang:  Account Log in:boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang:'))
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
        print('Please enter a password with the following: \n - Length: 8-18 characters long\n - Special character\n - Contains a lowercase letter\n - Contains an uppercase letter\n - Contains a number\n Enter password: ', end='')
    @staticmethod
    def get_street():
        print('**************************************************************')
        print('Street Address: \n - Format Examples:\n  - 1234 Address St \n  - 12345 6th st APT/UNIT 23\n  - 12 N Address Ave \nEnter Street Address: ' , end='')
    @staticmethod
    def get_city():
        print('**************************************************************')
        print("City: ", end='')
    @staticmethod
    def get_state():
        print('**************************************************************')
        print("State(2 Letters): ", end='')
    @staticmethod
    def get_zipcode():
        print('**************************************************************')
        print("Zipcode: ", end='')
    @staticmethod
    def get_login_password():
        print('**************************************************************')
        print("Password: ", end="")
    @staticmethod
    def create_user_success_msg():
        print(emoji.emojize("Registration success :thumbs_up:! Please Log in to your account."))
    @staticmethod
    def login_success_msg(name):
        os.system('cls')
        print(emoji.emojize(f":confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball:  Welcome {name}!  :confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball:"))
    @staticmethod
    def show_logged_in_menu():
        print(emoji.emojize('Please select from the choices below :down_arrow: '))
        print(emoji.emojize('1) Browse books by genre :glasses:'))
        print(emoji.emojize('2) Search books by author :glasses:'))
        print(emoji.emojize('3) Search books by title :glasses:'))
        print(emoji.emojize('4) Browse all books :books:'))
        print(emoji.emojize('5) View/edit cart :shopping_cart:'))
    @staticmethod
    def invalid_selection():
        print(emoji.emojize(":warning: Invalid menu selection. Please try again or enter '/q' to exit."))
        
