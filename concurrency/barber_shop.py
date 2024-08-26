import time
from threading import Condition

class BarberShop(object):
    def __init__(self):
        self.MAX_WAITING_CUSTOMERS = 3
        self.waiting_customers = 0
        self.waiting_for_barber = Condition()

    def customers_enter(self, cust_id):
        print("Customer with Id {} entered shop")
        if self.waiting_customers >= self.MAX_WAITING_CUSTOMERS:
            print("Since {} are waiting, customer {} returned from shop")
            return
        with self.waiting_for_barber:
            self.waiting_for_barber.acquire()
            self.waiting_for_barber.wait()


class CustomerSimulator(object):
    def __init__(self):
        self.barber_shop = BarberShop()

    def customer_generator(self):
        cust_id = 0
        while True:
            self.barber_shop.customers_enter(cust_id)
            time.sleep(2)
            cust_id += 1
