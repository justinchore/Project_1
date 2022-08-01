import mysql.connector
from mysql.connector import Error
import mysql_config  as c
import logging

class Book(object):
    def __init__(self):
        self.type = "Book"