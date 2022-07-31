import mysql.connector
from mysql.connector import Error
import mysql_config as c
import logging

class Order(object):
    def __init__(self) -> None:
        self.type = "Order"
        
    def create_order(self, customer_id):
        result = self.connect_to_db()
        if result == False:
            return False
        
        cnx = result[0]
        cursor = result[1]
        
        sql = "INSERT INTO Orders (customer_id) VALUES (%s)"
        vals = (customer_id)
        cursor.execute(sql, vals)
        
        cnx.commit()
        logging.info(f"New order (order_id: {cursor.lastrowid}) was inserted inton database...")
        print("1 record inserted, ID: ", cursor.lastrowid)
        
        cursor.close()
        cnx.close()
        return True
    
    def find_unpaid_order(self, cutsomer_id):
        pass
        
     
 
    def connect_to_db(self):
        try:
            cnx = mysql.connector.connect(host=c.host, database='test', user=c.user, password=c.password)
            if cnx.is_connected():
                print('Connecting to Server...')
                cursor = cnx.cursor()
                cursor.execute("select database();") 
                record = cursor.fetchone()
                print("Connected.")    
        except Error as e:
            print("Error: ", e)
            return False
        else:
            return [cnx, cursor]
        
    