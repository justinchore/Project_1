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
            return records
        except Error as e:
            msg = 'Failiure in executing query {0}. Error: {1}'.format(sql, e)
            return 'DB Error'
            
        