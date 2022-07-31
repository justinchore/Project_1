import mysql.connector
from mysql.connector import Error
import mysql_config as c
import logging

class Order(object):
    def __init__(self) -> None:
        self.type = "Order"
        
    