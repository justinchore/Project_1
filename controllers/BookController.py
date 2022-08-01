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
        self.validations = Validations.Validations()
    
    def book_menu(self, menu_choice):
        if menu_choice == 1:
            #Show genres
            pass
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