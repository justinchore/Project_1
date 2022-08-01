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
        print(emoji.emojize(':card_file_box:  :card_file_box:  :card_file_box:  :card_file_box:  GENRES :card_file_box:  :card_file_box:  :card_file_box:  :card_file_box:'))
        print(' ')
        for idx, g in enumerate(genres):
            print(f"{idx+1}.{g[1]}")
        print(' ')
        print(emoji.emojize("enter '/c' to acccess cart :shopping_cart:"))
        print(emoji.emojize("enter '/b' to go :BACK_arrow:"))
        print(' ')
        print('Select a genre number: ', end='')
    
        