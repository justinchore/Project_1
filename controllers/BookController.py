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
                    self.book_genres(result)
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
    
    def book_genres(self, result):
        print('From book controller -> book_genres', result)
        self.view.show_book_genres(result)
            