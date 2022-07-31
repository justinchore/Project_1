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
        
        sql = "INSERT INTO Orders (customer_id) VALUES (%s)"
        vals = (customer_id)
        cursor.execute(sql, vals)
        
        cnx.commit()
        logging.info(f"New order (order_id: {cursor.lastrowid}) was inserted into database...")
        print("1 record inserted, ID: ", cursor.lastrowid)
        
        record_id = cursor.lastrowid
        
        cursor.close()
        cnx.close()
        return record_id
    
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
        
    