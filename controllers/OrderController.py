import os
import emoji
import logging
import CustomExceptions
import validations.Validations as Validations
import views.OrderView as OrderView
import models.OrderModel as Order

class OrderController(object):
    def __init__(self):
        self.type = "OrderController"
        self.view = OrderView.OrderView()
        self.order_model = Order.Order()
        self.validations = Validations.Validations()
        self.order_id = None
        self.customer_id = None
        self.is_paid = None
        self.paid_date = None
        self.is_completed = None
        self.completed_date = None
    
    ####GETTERS#####
    def order_id(self):
        return self.order_id
    def customer_id(self):
        return self.customer_id
    def is_paid(self):
        return self.is_paid
    def paid_date(self):
        return self.paid_date
    def is_completed(self):
        return self.is_completed
    def completed_date(self):
        return self.completed_date
    
    ####SETTERS#####
    def set_order_id(self, id):
        self.order_id = id
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id
    def toggle_is_paid(self):
        self.is_paid = not self.is_paid
    def set_paid_date(self, date):
        self.paid_date = date
    def toggle_is_completed(self):
        self.is_completed = not self.is_completed
    def set_completed_date(self, completed_date):
        self.completed_date = completed_date
        
    
    def customer_initial_order_check(self, user_id):
        self.set_customer_id(user_id)
        print('inside customer_inital_order_check;', user_id)
        record = self.order_model.find_unpaid_order(user_id)
        if record == None:
            print('Customer does not have any open orders')
            record_id = self.order_model.create_order(user_id)
            record = self.order_model.get_order_by_id(record_id)
            self.set_order_id(record_id)
            print('Made a new order:', record)
            return record
        elif record == False:
            print('something went wrong')
        else:
            print('Customer has an open order')
            print('Order:', record)
            self.set_order_id(record['order_id'])
            return record
    
    def create_orderitem(self, book_id, order_quantity, price):
        orderitem_id = self.order_model.create_orderitem(self.order_id, book_id, order_quantity, price)
        if orderitem_id == True:
            return 'Success'
        elif orderitem_id == 'DB Error':
            return 'DB Error'
        
    def customer_orders(self, id):
        while True:
            try:
                orders = self.order_model.get_user_orders(id)
                print(orders)
                if orders == 'DB Error':
                    raise CustomExceptions.DatabaseError
                orderid_set = set()
                for o in orders: 
                    orderid_set.add(o['order_id'])
                self.view.show_customer_orders(orders)
                user_input = input().strip()
                if user_input.isalpha():
                    raise CustomExceptions.InvalidSelectionError
                elif user_input == '/b':
                    return 'BACK'
                elif user_input == '/q':
                    return 'Exit_Store'
                elif int(user_input) not in orderid_set:
                    raise CustomExceptions.InvalidSelectionError
                else: 
                    input_order_id = int(user_input)
                    self.order_details(input_order_id)
                
                
            except CustomExceptions.InvalidSelectionError as ise:
                self.view.invalid_selection()
            except CustomExceptions.DatabaseError as dbe:
                print(dbe.message)
                return 'BACK'
    
    def order_details(self, order_id):
        while True:
            try:
                print('in order details: order_id: ', order_id)
                orders = self.order_model.get_orderitems(order_id)
                if orders == 'DB Error':
                    raise CustomExceptions.DatabaseError
                self.view.show_order_orderitems(orders)
                user_input = input()
            except CustomExceptions.DatabaseError as dbe:
                print(dbe.message)
                
                
        

        
            