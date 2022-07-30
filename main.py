import mysql.connector
import mysql_config as c



class UserModel(object):
    def __init__(self, cnx, cursor) -> None:
        self.cnx = cnx
        self.cursor = cursor
    
    @property
    def cnx(self):
        return self.cnx
    
    @property
    def cursor(self):
        return self.cursor
    
    def close_cursor(self):
        self.cursor.close()
    
    def close_connection(self):
        self.cnx.close