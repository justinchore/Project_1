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
        self.validations = Validations.Validations()
    
    ###GETTERS######
    def genres(self):
        return self.genres
    ###SETTERS#####
    def set_genres(self, genre_dict):
        self.genres = genre_dict
    
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
        print('From book controller -> book_genres', records)
        #convert tuple to dict
        genre_dict = {}
        genre_interface_dict = {}
        #key = Genre, value = id
        for idx, r in enumerate(records):
            genre_dict[r[1]] = r[0]
            genre_interface_dict[idx+1] = r[1]
        #set created dictionary as a class attribute
        self.set_genres(genre_dict)
        print(genre_interface_dict)
        #prompt user for genre selection or back
        self.view.show_book_genres(records)
        user_input = input()
        
            