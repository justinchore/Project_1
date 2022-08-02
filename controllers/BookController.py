import os
import emoji
import logging
import CustomExceptions
import validations.Validations as Validations
import views.BookView as BookView
import models.BookModel as Book

class BookController(object):
    def __init__(self):
        self.type = "BookController"
        self.view = BookView.BookView()
        self.book_model = Book.Book()
        
        self.genres = None
        self.genre_interface_dict = None
        self.validations = Validations.Validations()
    
    ###GETTERS######
    def genres(self):
        return self.genres
    def genre_interface_dict(self):
        return self.genre_interface_dict
    ###SETTERS#####
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
                        return 'BACK'
                    if result == 'Exit Store':
                        return 'Exit Store'
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
        while True:
            try:
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
                if user_input == '/b':
                    return 'Back'
                elif user_input == '/c':
                    print('cart view not implemented')
                    return 'Back'
                elif int(user_input) not in self.genre_interface_dict:
                    raise CustomExceptions.InvalidSelectionError
                else:
                    user_input = int(user_input)
                    genre_name = genre_interface_dict[user_input]
                    print('You have chosen ', genre_name)
                    selected_genre_id = self.genres[genre_name]
                    result = self.filter_books(genre_name, 'GENRE')
                    if result == 'DB Error':
                        continue
            except CustomExceptions.InvalidSelectionError as ise:
                print(ise.message)
                os.system('cls')
                
    def filter_books(self, filter_data, filter_type):
        match filter_type:
            case 'GENRE':
                try:
                    result = self.book_model.get_books_by_genre(filter_data)
                    if result == 'DB Error':
                        raise CustomExceptions.DatabaseError
                    self.view.show_books(result)
                except CustomExceptions.DatabaseError as dbe:
                    self.view.book_error(dbe.message)
                    return 'Back'
            case 'AUTHOR':
                books = self.book_model.get_books_by_author(filter_data) 
            case 'AUTHOR_SEARCH':
                books = self.book_model.search_books_by_author(filter_data)
            case 'TITLE_SEARCH':
                books = self.book_model.search_books_by_title(filter_data)
            case 'ALL':
                books = self.book_model.get_all_books()
        
                
            
        
            