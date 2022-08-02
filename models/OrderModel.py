import mysql.connector
from mysql.connector import Error
import mysql_config as c
import logging

class Order(object):
    def __init__(self) -> None:
        self.type = "Order"
        
    def create_order(self, customer_id):
        cnx = self.connect_to_db()
        if cnx == False: #connection didnt happen
            return False
        
        cursor = cnx.cursor()
        
        sql = f"INSERT INTO Orders (customer_id) VALUES ({customer_id})"
        cursor.execute(sql)
        
        cnx.commit()
        logging.info(f"New order (order_id: {cursor.lastrowid}) was inserted into database...")
        print("1 record inserted, ID: ", cursor.lastrowid)
        
        record_id = cursor.lastrowid
        
        cursor.close()
        cnx.close()
        return record_id
    
    def create_orderitem(self, order_id, book_id, quantity, book_price):
        try: 
            cnx = self.connect_to_db()
            cursor = cnx.cursor()
            #Check for same book inside order
            sql = f"SELECT order_id, quantity From OrderItems WHERE book_id = {book_id}"
            cursor.execute(sql)
            record = cursor.fetchone()
            if record != None:
                prev_quantity = record[1]
                sql1 = f"UPDATE OrderItems SET quantity = {prev_quantity + quantity}"
                cursor.execute(sql1)
                logging.info("Duplicate book found in orderItems. Updated the quantity instead of creating new order")
            else: 
                sql2 = "INSERT INTO OrderItems (order_id, book_id, quantity, book_price) VALUES (%s, %s, %s, %s)"
                values = (order_id, book_id, quantity, book_price)
                cursor.execute(sql2, values)
                logging.info(f"New orderItem (id: {cursor.lastrowid}) was inserted into database...")
                print('1 record inserted, ID: ', cursor.lastrowid)
                
            cnx.commit()         
            cursor.close()
            cnx.close()
            return True
        
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error'
    
    def find_unpaid_order(self, customer_id):
        cnx = self.connect_to_db()
        if cnx == False: #connection didnt happen
            return False
        cursor = cnx.cursor(dictionary=True)
        sql = f"SELECT * FROM Orders WHERE customer_id = {customer_id} AND is_paid = {False}"
        cursor.execute(sql)
        record = cursor.fetchone()
        
        cursor.close()
        cnx.close()
        
        return record
        
    def get_order_by_id(self, order_id):
        cnx = self.connect_to_db()
        cursor = cnx.cursor(dictionary=True)
        
        sql = f"SELECT * FROM Orders WHERE order_id = {order_id}"
        cursor.execute(sql)
        record = cursor.fetchone()
        
        cursor.close()
        cnx.close()
        
        if record != None:
            return record
        else:
            return False
        
        
    
    def connect_to_db(self):
        try:
            cnx = mysql.connector.connect(host=c.host, database='test', user=c.user, password=c.password)
            if cnx.is_connected():
                print('Connecting to Server...')
                print("Connected.")    
        except Error as e:
            print("Error: ", e)
            return False
        else:
            return cnx
        
    