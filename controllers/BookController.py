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
    
    def log_in_menu(self):
        pass