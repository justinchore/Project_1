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
        
            