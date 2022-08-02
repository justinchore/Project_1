import mysql.connector
from mysql.connector import Error
import mysql_config  as c
import logging

class Book(object):
    def __init__(self):
        self.type = "Book"
        
    def connect_to_db(self):
        try:
            cnx = mysql.connector.connect(host=c.host, database='test', user=c.user, password=c.password)
            if cnx.is_connected():
                print('Connecting to Server...')
                print('Connected.')
            
        except Error as e:
            print("Error: ", e)
            return False
        else:
            return cnx
    
    def get_all_genres(self):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor()
            sql = "SELECT * FROM Genres"
            cursor.execute(sql)
            records = cursor.fetchall()
            cursor.close()
            cnx.close()
            return records
        except Error as e:
            msg = 'Failiure in executing query {0}. Error: {1}'.format(sql, e)
            return 'DB Error'
        
    def get_books_by_genre(self, data, page_number, books_per_page):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            sql = f"SELECT * FROM books_view WHERE genre_id = {data} LIMIT {books_per_page} OFFSET {books_per_page * (page_number - 1)}"
            cursor.execute(sql)
            records = cursor.fetchall()
            cursor.close()
            cnx.close()
            return records
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error'
    def search_books_by_author(self, data):
        pass
    def search_books_by_title(self, data):
        pass
    def get_all_books(self):
        pass
    
    def get_book_by_id(self, id):
        try: 
            cnx = self.connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            sql = f"SELECT * FROM books_view WHERE book_id = {id}"
            cursor.execute(sql)
            record = cursor.fetchone()
            return record
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error'
    
    def change_inventory_by_id(self, book_id, book_stock, quantity):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor()
            sql = f"UPDATE Books SET stock = {book_stock + quantity} WHERE book_id = {book_id}"
            cursor.execute(sql)
            cnx.commit()
            logging.info(f"{cursor.rowcount}) record was updated in the database...")
            cursor.close()
            cnx.close()
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error'
            
            
        