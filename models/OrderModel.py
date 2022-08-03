import mysql.connector
from mysql.connector import Error
import mysql_config as c
import logging
from datetime import datetime

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
    
    def get_user_orders(self, user_id):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            sql = f"SELECT * FROM Orders WHERE customer_id = {user_id} AND is_paid = True ORDER BY order_id DESC"
            cursor.execute(sql)
            records = cursor.fetchall()
            cursor.close()
            cnx.close()
            return records
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error' 
    
    def get_orderitems(self, order_id):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            sql = f"SELECT oi.orderItem_id, b.book_id, b.book_title, CONCAT(a.author_fname,' ',a.author_lname) as author, oi.quantity, oi.book_price FROM OrderItems as oi JOIN Orders as o JOIN Books as b JOIN Authors as a ON oi.order_id = o.order_id AND oi.book_id = b.book_id AND b.author_id = a.author_id WHERE o.order_id = {order_id}"
            cursor.execute(sql)
            records = cursor.fetchall()
            cursor.close()
            cnx.close()
            return records
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error' 
    
    def get_book_from_orderitem(self, orderitem_id):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor(dictionary=True)
            sql = f"SELECT * FROM Books JOIN OrderItems ON Books.book_id = OrderItems.book_id WHERE orderItem_id = {orderitem_id}"
            cursor.execute(sql)
            record = cursor.fetchone()
            cursor.close()
            cnx.close()
            return record
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error' 
    
    def change_orderitem_quantity(self, orderitem_id, q_value, current_stock, book_id):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor()
            sql = f"UPDATE Books SET stock = (({current_stock} + (SELECT quantity FROM OrderItems WHERE orderItem_id = {orderitem_id})) - {q_value}) WHERE book_id = {book_id}"
            cursor.execute(sql)
            sql = f"UPDATE OrderItems SET quantity = {q_value} WHERE orderItem_id = {orderitem_id}"
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
            logging.info(f"{cursor.rowcount}) record was updated in the database...")
            return True
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error'
        
    def get_order_total(self, order_id):
        try: 
            cnx = self.connect_to_db()
            cursor = cnx.cursor()
            sql = f"SELECT SUM(quantity * book_price) as total FROM OrderItems WHERE order_id = {order_id}"
            cursor.execute(sql)
            total = cursor.fetchone()
            cursor.close()
            cnx.close()
            return total
        except Error as e:
            msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
            print(msg)
            return 'DB Error' 
        
    def checkout_order(self, order_id, customer_id):
        try:
            cnx = self.connect_to_db()
            cursor = cnx.cursor()
            now = datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            sql = f"UPDATE Orders SET is_paid = True, paid_date='{formatted_date}' WHERE order_id = {order_id}"
            cursor.execute(sql)
            sql = f"INSERT INTO Orders (customer_id) VALUES ({customer_id})"
            cursor.execute(sql)
            cnx.commit()
            new_order_id = cursor.lastrowid
            logging.info(f"New orderItem (id: {cursor.lastrowid}) was inserted into database...")
            print('1 record inserted, ID: ', cursor.lastrowid)
            cursor.close()
            cnx.close()

            return new_order_id
        except Error as e:
            msg = 'Failure in executing query {0}. Error {1}'.format(sql, e)
            print(msg)
            return 'DB Error'    
            
            
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
        
#  try: 
#     cnx = self.connect_to_db()
#     cursor = cnx.cursor(dictionary=True)
#     sql = f"SELECT * FROM books_view WHERE book_id = {id}"
#     cursor.execute(sql)
#     record = cursor.fetchone()
#     return record
# except Error as e:
#     msg = 'Failure in executing query {0}. Error: {1}'.format(sql, e)
#     print(msg)
#     return 'DB Error'
    