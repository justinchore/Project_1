import os
import emoji
import logging
import CustomExceptions
import validations.Validations as Validations
import views.BookView as BookView
import models.BookModel as Book

class BookController(object):
    def __init__(self, order_controller):
        self.type = "BookController"
        self.view = BookView.BookView()
        self.order_controller = order_controller
        self.book_model = Book.Book()
        self.page_number = 1
        self.books_per_page = 10
        self.browsing = True
        self.genres = None
        self.genre_interface_dict = None
        self.is_first_page = True
        self.is_last_page = False
        self.validations = Validations.Validations()
    
    ###GETTERS######
    def is_first_page(self):
        return self.first_page
    def is_last_page(self):
        return self.last_page
    def page_number(self):
        return self.page_number
    def books_per_page(self):
        return self.books_per_page
    def genres(self):
        return self.genres
    def genre_interface_dict(self):
        return self.genre_interface_dict
    ###SETTERS#####
    def set_is_first_page(self, value):
        self.is_first_page = value
    def set_is_last_page(self, value):
        self.is_last_page = value
    def set_browsing(self, value):
        self.browsing = value
    def set_page_number(self, value):
        self.page_number = value
    def set_genres(self, genre_dict):
        self.genres = genre_dict
    def set_genre_interface_dict(self, genre_interface_dict):
        self.genre_interface_dict = genre_interface_dict
    
    def book_menu(self, menu_choice):
        menu_choice = int(menu_choice)
        while True:
            if menu_choice == 1:
                try:
                    result = self.book_model.get_all_genres()
                    if result == 'DB Error':
                        raise CustomExceptions.DatabaseError
                except CustomExceptions.DatabaseError as dbe:
                    self.view.book_error(dbe.message)
                else:
                    result = self.book_genres(result)
                    if result == 'BACK':
                        os.system('cls')
                        return 'BACK'
                    if result == 'Exit_Store':
                        return 'Exit_Store'
            elif menu_choice == 2:
                #present all authors to the user (alph)
                #have search functionality
                pass
            elif menu_choice == 3:
                #search by title
                pass
            elif menu_choice == 4:
                #all books with page number?
                pass
    
    def book_genres(self, records):
        os.system('cls')
        while True:
            try:
                # os.system('cls')
                records = self.book_model.get_all_genres()
                genre_dict = {}
                genre_interface_dict = {}
                #key = Genre, value = id
                for idx, r in enumerate(records):
                    genre_dict[r[1]] = r[0]
                    genre_interface_dict[idx+1] = r[1]
                #set created dictionary as a class attribute
                self.set_genres(genre_dict)
                self.set_genre_interface_dict(genre_interface_dict)
                #prompt user for genre selection or back
                self.view.show_book_genres(records)
                user_input = input()
                if user_input == '/q':
                    os.system('cls')
                    return 'Exit_Store'
                if user_input == '/b':
                    os.system('cls')
                    return 'BACK'
                elif user_input == '/c':
                    result = self.order_controller.see_cart()
                    if result == 'BACK':
                        os.system('cls')
                        continue
                    if result == 'Exit_Store':
                        os.system('cls')
                        return 'Exit_Store'
                elif user_input.isalpha() == True:
                    raise CustomExceptions.InvalidSelectionError
                elif user_input.isdigit() == False:
                    raise CustomExceptions.InvalidSelectionError
                elif int(user_input) not in self.genre_interface_dict:
                    raise CustomExceptions.InvalidSelectionError
                else:
                    user_input = int(user_input)
                    genre_name = genre_interface_dict[user_input]
                    selected_genre_id = self.genres[genre_name]
                    result = self.filter_books(selected_genre_id, 'GENRE')
                    if result == 'DB Error':
                        continue
                    if result == 'BACK':
                        continue
                    if result == 'Exit_Store':
                        return 'Exit_Store'
            except CustomExceptions.InvalidSelectionError as ise:
                print(ise.message)
                os.system('cls')
                
    def filter_books(self, filter_data, filter_type):
        os.system('cls')
        self.set_browsing(True)
        self.set_is_first_page(True)
        self.set_is_last_page(False)
        self.set_page_number(1)
        # while True:
        match filter_type:
                case 'GENRE':
                     while self.browsing == True: 
                        try:
                            # os.system('cls')
                            # print('back to top')
                            print(f'Page #: {self.page_number}')
                            pn = self.page_number
                            # print('Page Number:', pn)
                            bpp = self.books_per_page
                            # print('Books Per Page:', bpp)
                            result = self.book_model.get_books_by_genre(filter_data,pn, bpp)
                            if result == 'DB Error':
                                raise CustomExceptions.DatabaseError
                            if len(result) < self.books_per_page:
                                self.set_is_last_page(True)
                            if self.page_number == 1:
                                self.set_is_first_page(True)
                            else:
                                self.set_is_first_page(False)
                                
                            # print(f'is_first_page: {self.is_first_page}')
                            # print(f'is_last_page: {self.is_last_page}')
                            self.view.show_books(result, self.page_number, self.is_first_page, self.is_last_page)
                            book_ids_list = []
                            for book in result:
                                book_ids_list.append(book['book_id'])
                            user_input = input()
                            if (self.is_first_page == True) and (self.is_last_page == False):
                                # print('First page but not last page')
                                if user_input == '/n':
                                    self.set_page_number(self.page_number + 1)
                                    os.system('cls')
                                    continue
                                if user_input == '/p':
                                    raise CustomExceptions.InvalidSelectionError
                                elif user_input.isalpha():
                                    raise CustomExceptions.InvalidSelectionError
                                # elif user_input.isdigit() == False:
                                #     raise CustomExceptions.InvalidSelectionError
                            elif (self.is_first_page == False) and (self.is_last_page == False):
                                # print('Not first page or last page')
                                if user_input == '/n':
                                    self.set_page_number(self.page_number + 1)
                                    os.system('cls')
                                    continue
                                elif user_input == '/p':
                                    self.set_page_number(self.page_number - 1)
                                    os.system('cls')
                                    continue
                                elif user_input.isalpha():
                                    raise CustomExceptions.InvalidSelectionError
                                # elif user_input.isdigit() == False:
                                #     raise CustomExceptions.InvalidSelectionError
                            elif (self.is_first_page == False) and (self.is_last_page == True):
                                print('last page')
                                if user_input == '/p':
                                    self.set_is_last_page(False)
                                    self.set_page_number(self.page_number - 1)
                                    os.system('cls')
                                    continue
                                elif user_input == '/n':
                                    raise CustomExceptions.InvalidSelectionError
                                elif user_input.isalpha() == True:
                                    raise CustomExceptions.InvalidSelectionError
                            else:
                                if user_input.isalpha() == True:
                                    raise CustomExceptions.InvalidSelectionError
                            # print('page number outside')
                            if user_input == '/b':
                                os.system('cls')
                                return 'BACK'
                            elif user_input == '/q':
                                os.system('cls')
                                print('Exiting...')
                                return 'Exit_Store'
                            elif user_input == '/c':
                                result = self.order_controller.see_cart()
                                if result == 'BACK':
                                    continue
                                elif result == 'Exit_Store':
                                    os.system('cls')
                                    print('Exiting...')
                                    return 'Exit_Store'   
                            elif user_input.isdigit() == False:
                                raise CustomExceptions.InvalidSelectionError
                            elif int(user_input) not in book_ids_list:
                                # print('Not in idslist')
                                raise CustomExceptions.InvalidSelectionError
                            result = self.book_details(int(user_input))
                            if result == 'BACK':
                                continue
                            if result == 'BACK_TO_MENU':
                                os.system('cls')
                                return 'BACK'
                            elif result == 'Exit_Store':
                                os.system('cls')
                                print('Exiting...')
                                return 'Exit_Store'
                            break
                                
                        except CustomExceptions.DatabaseError as dbe:
                            os.system('cls')
                            self.view.show_book_error(dbe.message)
                        except CustomExceptions.InvalidSelectionError as ise:
                            os.system('cls')
                            self.view.invalid_selection()
                case 'AUTHOR_SEARCH':
                    books = self.book_model.search_books_by_author(filter_data)
                case 'TITLE_SEARCH':
                    books = self.book_model.search_books_by_title(filter_data)
                case 'ALL':
                    books = self.book_model.get_all_books()
    def book_details(self,book_id):
        os.system('cls')
        while True:
            try:
                book = self.book_model.get_book_by_id(book_id)
                if book == 'DB Error':
                    raise CustomExceptions.DatabaseError
                book_stock = book["stock"]
                book_price = book["book_price"]
                self.view.show_book_details(book)
                user_input = input().strip()
                if user_input.isalpha():
                    raise CustomExceptions.InvalidSelectionError
                elif user_input == '/b':
                    os.system('cls')
                    return 'BACK'
                elif user_input == '/q':
                    os.system('cls')
                    print('Exiting...')
                    return 'Exit_Store'
                elif user_input.isdigit() == False:
                    raise CustomExceptions.InvalidSelectionError
                
                user_quantity = int(user_input) 
                if int(user_input) > book_stock:
                    raise CustomExceptions.QuantityError
                
                result = self.book_model.change_inventory_by_id(book_id, book_stock, user_quantity*-1)
                if result == 'DB Error':
                    raise CustomExceptions.DatabaseError
                else: 
                    result = self.order_controller.create_orderitem(book_id, user_quantity,book_price)
                    if result == True:
                        os.system('cls')
                        return 'BACK'
                    elif result == 'DB Error':
                        raise CustomExceptions.DatabaseError
                
            except CustomExceptions.DatabaseError as deb:
                os.system('cls')
                self.view.show_book_error(deb.message)
            except CustomExceptions.InvalidSelectionError as ise:
                os.system('cls')
                self.view.invalid_selection()
            except CustomExceptions.QuantityError as qe:
                os.system('cls')
                print(emoji.emojize(f":warning:  {qe.message}"))
                
                
        
                
            
        
            