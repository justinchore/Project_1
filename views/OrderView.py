import emoji
import os
from prettytable import PrettyTable
from decimal import Decimal

class OrderView(object):
    @staticmethod
    def show_customer_orders(orders):
        if len(orders) == 0:
            print('No orders to display.')
        else:
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
        if (len(orders) > 0):
            print('- or enter OrderID for details: ', end='')
        else:
            print('--input: ', end='')
    @staticmethod
    def admin_orders_view(orders):
        # print(orders)
        if len(orders) == 0:
            print('No orders to display.')
        else:
            orders_table = PrettyTable()
            orders_table.field_names = ["OrderID", "UserEmail", "Paid","PaidDate", "Completed", "CompletedDate" ]
            for o in orders:
                orders_table.add_row([
                    o['order_id'],
                    o['email_address'],
                    o['is_paid'] == True,
                    o['paid_date'],
                    o['is_completed'] == True,
                    o['completed_date']
                ])
            print(orders_table)
        print(emoji.emojize('/b: go back:BACK_arrow:'))
        print(emoji.emojize('/q: exit store :victory_hand:'))
        # print('- or enter OrderID for details: ', end='')
    @staticmethod
    def show_order_orderitems(orderitems):
        orderitems_table = PrettyTable()
        orderitems_table.field_names = ["OrderItemID", "Title", "Author", "Quantity", "Price"]
        total_order_price = Decimal(0.00)
        for item in orderitems:
            orderitems_table.add_row([
                item['orderItem_id'],
                item['book_title'],
                item['author'],
                item['quantity'],
                item['book_price']
                ])
            total_order_price += (item['book_price']*item['quantity'])
        orderitems_table.add_row(['--', '-- ', '-- ', 'Total Price:', total_order_price])
        print(orderitems_table)
        print('')
        print(emoji.emojize('/b: go back to menu:BACK_arrow:'))
        print(emoji.emojize('/q: exit store :victory_hand:'))
        
    @staticmethod
    def show_current_orderitems(orderitems, has_items):
        OrderView.show_order_orderitems(orderitems)
        if (has_items):
            print(emoji.emojize('/c: checkout :money_with_wings:'))
            print('- or enter OrderitemID to change quantity: ', end='')
        else:
            print('--input: ', end='')
        
    @staticmethod
    def checkout_view(total):
        print(f'TOTAL AMOUNT DUE: ${total} ')
        print('Pay amount? (y/n): ', end='')
        
    @staticmethod
    def basic_input():
        print('input: ', end='')
        
    @staticmethod
    def order_edit_change_quantity(book_title,stock):
        print(f"--enter in the new quantity for '{book_title}' (current stock: {stock}): ", end='')
        
    @staticmethod
    def show_customer_cart():
        pass
    @staticmethod
    def invalid_selection():
        print(emoji.emojize(":warning: Invalid menu selection. Please try again or enter '/q' to exit."))
