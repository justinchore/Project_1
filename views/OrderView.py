import emoji
import os
from prettytable import PrettyTable

class OrderView(object):
    @staticmethod
    def show_customer_orders(orders):
        orders_table = PrettyTable()
        orders_table.field_names = ["OrderID", "PaidDate", "Completed", "CompletedDate" ]
        for o in orders:
            orders_table.add_row([
                o['order_id'],
                o['paid_date'],
                o['is_completed'] == True,
                o['completed_date']
            ])
        print(orders_table)
        print(emoji.emojize('/b: go back:BACK_arrow:'))
        print(emoji.emojize('/q: exit store :victory_hand:'))
        print("Enter order id for details:", end="")
    @staticmethod
    def show_order_orderitems(orderitems):
        orderitems_table = PrettyTable()
        print(orderitems)
    @staticmethod
    def show_customer_cart():
        pass
    @staticmethod
    def invalid_selection():
        print(emoji.emojize(":warning: Invalid menu selection. Please try again or enter '/q' to exit."))
