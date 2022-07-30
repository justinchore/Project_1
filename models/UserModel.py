import mysql.connector
from mysql.connector import Error
import mysql_config as c
import uuid

class User(object):
    def __init__(self) -> None:
        self.type = "User"
    
    # def cnx(self):
    #     return self.cnx

    # def cursor(self):
    #     return self.cursor
        
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
        
        uuid_id = uuid.uuid4()
        sql = "INSERT INTO Users(user_id, first_name, last_name, email_address, password, address)"
        vals = ({uuid_id},'{fname}','{lname}', '{email}', '{password}', '{address}')
        cursor.execute(sql, vals)
            
        cnx.commit()
        print('1 record inserted, ID: ', cursor.lastrowid)
        
        cursor.close()
        cnx.close()
        return True
        