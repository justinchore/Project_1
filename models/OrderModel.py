import mysql.connector
from mysql.connector import Error
import mysql_config as c
import logging

class Order(Object):
    def __init__(self) -> None:
        self.type = "Order"
        
    