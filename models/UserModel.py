import mysql.connector
from mysql.connector import Error
import mysql_config as c
import uuid
import bcrypt
import logging

class User(object):
    def __init__(self) -> None:
        self.type = "User"
    
    # def cnx(self):
    #     return self.cnx

    # def cursor(self):
    #     return self.cursor
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
        
    def create_user(self, fname, lname, email, password, address):
        try:
            cnx = mysql.connector.connect(host=c.host,
                                         database='test',
                                         user=c.user,
                                         password=c.password)
            if cnx.is_connected():
                db_Info = cnx.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = cnx.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        else:
            pass
        
        # cnx = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database='test')
        # cursor = cnx.cursor()
        
        cursor = cnx.cursor()
        sql = "INSERT INTO Users (first_name, last_name, email_address, is_admin, password, address) VALUES (%s, %s, %s, %s, %s, %s)"
        vals = (fname, lname, email, False, password, address) 
        cursor.execute(sql, vals)
        
        # sql = "INSERT INTO Users (first_name, last_name, email_address, is_admin, password, address) VALUES (%s, %s, %s, %s, %s, %s)"
        # vals = (fname, lname, email, False, password, address) 
        # cursor.execute(sql, vals)
            
        cnx.commit()
        logging.info(f"New user (id: {cursor.lastrowid}) was inserted into database...")
        print('1 record inserted, ID: ', cursor.lastrowid)
        
        cursor.close()
        cnx.close()
        return True
    def get_all_users(self, user_id):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            sql = f"SELECT * FROM Users WHERE user_id != {user_id}"
            cursor.execute(sql)
            logging.info("ADMIN: All Users retrieved from Database")
            users = cursor.fetchall()
            cursor.close()
            cnx.close()
            return users
        except Error as e:
            msg = 'Failiure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error'
            
    
    def get_user_by_email(self, email):
        try:
            cnx = mysql.connector.connect(host=c.host,
                                         database='test',
                                         user=c.user,
                                         password=c.password)
            if cnx.is_connected():
                db_Info = cnx.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = cnx.cursor(dictionary=True)
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                logging.info("Accessed database in get_user_by_email function...")

        except Error as e:
            print("Error while connecting to MySQL", e)
        else:
            pass
        
        sql = f"SELECT * FROM Users WHERE email_address = '{email}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        cnx.close()
        return result
    
    def get_admin_genres(self):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            sql = "SELECT * FROM Genres"
            cursor.execute(sql)
            records = cursor.fetchall()
            cursor.close()
            cnx.close()
            return records
        except Error as e:
            msg = 'Failiure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error'
        
    
    @staticmethod
    def hash_password(chars):
        bytes = chars.encode('utf-8')
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(bytes, salt)
    
    @staticmethod
    def password_auth(attempt, pw_string):
        password_str_byte = pw_string.encode('utf-8')
        return bcrypt.checkpw(attempt.encode('utf-8'), password_str_byte)


        
        