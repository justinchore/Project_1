import emoji
import os
from prettytable import PrettyTable

class BookView(object):
    @staticmethod
    def show_books(books, page_number, first_page, last_page):
        print('Show books view')
        print('Page Number: ' ,page_number)
        print('How Many Books: ', len(books))
        book_table = PrettyTable()
        book_table.field_names = ["ID", "Title", "Author", "Genre", "Price", "Stock" ]
        for idx, b in enumerate(books):
            book_table.add_row([
                b['book_id'],
                b['book_title'],
                b['author_name'],
                b['genre_name'],
                b['book_price'],
                b['stock']
            ])
        print(book_table)
        if (first_page == True) and (last_page == False):
            print('/n: next page')
        elif (first_page == False) and (last_page == False):
            print('/n: next page')
            print('/p: prev page')
        elif (first_page == False) and (last_page == True):
            print('/p: prev page')
        
        print('/b: back to genres')
        print(emoji.emojize("/q: exit store:victory_hand:"))
        print(emoji.emojize("/c: cart:shopping_cart:"))
        print('////////////////////////////')
        print('--select book by ID: ', end="")

    @staticmethod
    def show_book_error(msg):
        print(emoji.emojize(f":warning:  {msg}"))
    @staticmethod
    def show_book_genres(genres):
        print(emoji.emojize(':card_file_box:  :card_file_box:  :card_file_box:  :card_file_box:  GENRES :card_file_box:  :card_file_box:  :card_file_box:  :card_file_box:'))
        print(' ')
        for idx, g in enumerate(genres):
            print(f"{idx+1}.{g[1]}")
        print(' ')
        print(emoji.emojize("/c: cart:shopping_cart:"))
        print(emoji.emojize("/b: go back:BACK_arrow:"))
        print(emoji.emojize("/q: exit store:victory_hand:"))
        print('- or select a genre number: ', end='')
    @staticmethod
    def invalid_selection():
        print(emoji.emojize(":warning: Invalid menu selection. Please try again or enter '/q' to exit."))
    @staticmethod
    def show_book_details(book):
        print('**************************************')
        title = book.get('book_title')
        author = book.get('author_name')
        book_info = book.get('book_description')
        price = book.get('book_price')
        stock = book.get('stock')
        book_table = PrettyTable()
        book_table.field_names = [f'{title} by {author}']
        book_table.add_row([book_info])
        book_table.add_row([' '])
        book_table.add_row([f'Price: ${price}'])
        book_table.add_row([f'Stock: {stock}'])
        # print(f'{title} by {author}', end='\n\n')
        # print(f'{book_info}', end="\n\n")
        # print(f"Price: ${price}")
        # print(f"Stock: {stock}" )
        # print('**************************************')
        book_table._max_width = {f'{title} by {author}': 50}
        print(book_table)
        print('/b: back to books')
        print('/q: Exit Store')
        print('To place into cart, enter desired quantity:', end="")
        
        
        
    
        