import emoji
import os

class BookView(object):
    @staticmethod
    def show_books():
        pass
    @staticmethod
    def book_error(msg):
        print(emoji.emojize(f":warning: {msg}"))
    @staticmethod
    def book_genres(genres):
        for g in genres:
            print(g)