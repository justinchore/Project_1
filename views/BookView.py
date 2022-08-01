import emoji
import os

class BookView(object):
    @staticmethod
    def show_books():
        pass
    @staticmethod
    def show_book_error(msg):
        print(emoji.emojize(f":warning: {msg}"))
    @staticmethod
    def show_book_genres(genres):
        for idx, g in enumerate(genres):
            print(idx+1, '.' , g[1])