import emoji
import os
from prettytable import PrettyTable

class OrderView(object):
    @staticmethod
    def show_customer_orders(orders):
        orders_table = PrettyTable()
        orders_table.field_names = ["OrderID"]
    @staticmethod
    def show_customer_cart():
        pass
