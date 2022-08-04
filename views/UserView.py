import emoji
import os
from prettytable import PrettyTable

class UserView(object):
    @staticmethod
    def welcome_message():
        os.system
        print(emoji.emojize(":derelict_house: :derelict_house: :derelict_house:  The Little Command Line Book Store on the Corner :derelict_house: :derelict_house: :derelict_house:"))
        print('-----------------------------------------------------------------')
        print(emoji.emojize('Please select from the following:'))
        print(emoji.emojize('1) Log in to your account :door:'))
        print(emoji.emojize('2) Create an account :NEW_button:'))
        print(emoji.emojize('3) Exit store :victory_hand:'))
    
    ######Views for getting user information for creation/login
    
    @staticmethod
    def login_message():
        print(emoji.emojize(':boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang:  Account Log in:boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang: :boomerang:'))
    @staticmethod
    def get_firstname():
        print('------------------------------------------------------')
        print("First name: ", end='')
    @staticmethod
    def get_lastname():
        print('-------------------------------------------------------')
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
        # os.system('cls')
        print(emoji.emojize(f":confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball:  Welcome {name}!  :confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball:"))
        print('**************************************************************')
    
    @staticmethod
    def show_logged_in_menu():
        print(emoji.emojize('Please select from the choices below:down_arrow: '))
        print(emoji.emojize('1) Browse books by genre:glasses:'))
        # print(emoji.emojize('2) Search books by author:glasses:'))
        # print(emoji.emojize('3) Search books by title:glasses:'))
        # print(emoji.emojize('4) Browse all books:books:'))
        print(emoji.emojize('2) Order History:linked_paperclips:'))
        print('\n')
        print(emoji.emojize("/c: cart:shopping_cart:"))
        print(emoji.emojize("/q: exit store:victory_hand:"))
    
    @staticmethod
    def show_admin_logged_in_menu():
        print(emoji.emojize('Please select from the choices below:down_arrow: '))
        # print(emoji.emojize('1) Manage Books'))
        print(emoji.emojize('1) Manage Orders'))
        print(emoji.emojize('2) Admin Permissions'))
        print(emoji.emojize("/q: exit :victory_hand:"))
        
    @staticmethod
    # def show_admin_book_manager():
    #     print(emoji.emojize('Book Manager :down_arrow: '))
    #     print(emoji.emojize('1) Add a Book'))
    #     print(emoji.emojize('2) Book search'))
    #     # print(emoji.emojize('3) Stock Warning'))
    #     print(emoji.emojize('/b: go back:BACK_arrow:'))
    #     print(emoji.emojize("/q: exit :victory_hand:"))
    #     print('--input:', end='')
    
    @staticmethod
    def show_admin_order_manager():
        print(emoji.emojize('ORDER MANAGER :down_arrow: '))
        print(emoji.emojize('1) See all orders'))
        # print(emoji.emojize('2) Update order'))
        # print(emoji.emojize('3) Delete order'))
        # print(emoji.emojize('3) Stock Warning'))
        print(emoji.emojize('/b: go back:BACK_arrow:'))
        print(emoji.emojize("/q: exit :victory_hand:"))
        print('--input:', end='')
    
    @staticmethod
    def show_admin_permissions_manager():
        print(emoji.emojize('PERMISSIONS MANAGER:down_arrow: '))
        print(emoji.emojize('1) Update Permissions'))
        print(emoji.emojize('2) See all users'))
        # print(emoji.emojize('3) Stock Warning'))
        print(emoji.emojize('/b: go back:BACK_arrow:'))
        print(emoji.emojize("/q: exit :victory_hand:"))
        print('--input:', end='')
        
    @staticmethod
    def show_admin_genres(genres):
        genre_table = PrettyTable()
        genre_table.field_names = ['genreID', 'Genre']
        for g in genres:
            genre_table.add_row([
                g['genre_id'],
                g['genre_name']
            ])
        print(genre_table)
        print(emoji.emojize('/b: go back to menu:BACK_arrow:'))
        print(emoji.emojize("/q: exit :victory_hand:"))
        print('-or enter genreID: ', end='')
            
    @staticmethod
    def admin_show_all_users(users):
        users_table = PrettyTable()
        users_table.field_names = ['userID', 'Name', 'Email', 'Admin', 'Address']
        for user in users:
            users_table.add_row([
                user['user_id'],
                f"{user['first_name']} {user['last_name']}",
                user['email_address'],
                user['is_admin'] == True,
                user['address']
            ])
        print(users_table)
        print(emoji.emojize('/b: go back:BACK_arrow:'))
        print(emoji.emojize("/q: exit :victory_hand:"))
        print('--input:', end='')
        
    @staticmethod
    def get_book_author_fname():
        print("Author's first name: ", end='')
    @staticmethod
    def get_book_author_lname():
        print("Author's last name: ", end='')
    @staticmethod
    def get_book_title():
        print("Enter Title: ", end='')
    @staticmethod
    def get_book_description():
        print("Enter description(Min. 300 characters): ", end='')
    @staticmethod
    def get_book_price():
        print("Enter book price (formats: [5, 5.99, 25.05]: ", end='')
    @staticmethod
    def get_book_genre():
        print("Author's first name: $", end='')
        
        
    
        
        
    @staticmethod
    def invalid_selection():
        print(emoji.emojize(":warning: Invalid menu selection. Please try again or enter '/q' to exit."))
    
    
    
        
