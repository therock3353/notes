import abc

class PaymentMethod(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(PaymentMethod):

    def process_payment(self, amount):
        print "processed payment {} using cash".format(amount)

class CreditCardPayment(PaymentMethod):

    def process_payment(self, amount):
        print "processed payment {} using card".format(amount)

class PaymentFactory(object):
    __methods = {
        'credit_card': CreditCardPayment,
        'cash': CashPayment
    }

    def __get_payment_processor(self, payment_method):
        if payment_method not in PaymentFactory.__methods:
            raise Exception("payment method is not supported")
        payment_method_class = PaymentFactory.__methods.get(payment_method)
        return payment_method_class()


class BaseVendingMachine(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def purchase(self, key):
        pass

    @abc.abstractmethod
    def load_machine(self):
        pass

    @abc.abstractmethod
    def __dispatch(self, key):
        pass

class PricingProvider(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def price(self, item):
        pass

class StaticPricingProvider(object):
    #eveny item in the shelf is 1$
    def price(self, item):
        return 1

class DynamicPricingProvider(object):

    def price(self, item):
        pass

class VendingMachine(BaseVendingMachine):
    def __init__(self):
        self.num_rows = 5
        self.num_cols = 5
        self.default_item_count = 2
        self.pricing_provider = StaticPricingProvider()
        self.payment_processor = None
        self.items = []
        self.load_machine()

    def load_machine(self):
        for row_id in range(self.num_rows):
            row = []
            for col_id in range(self.num_cols):
                row.append(self.default_item_count)
            self.items.append(row)
        print self.items
        
    def purchase(self, key, payment_method):
        self.validate(key)# validate that item exists in vending machine
        amount = self.pricing_provider.price(key)
        payment_processor = self.get_payment_processor()
        if self.payment_processor.pay(amount) is True:
            self.__dispatch(key)

    def validate(self, key):
        pass

    def __dispatch(self, key):
        row_id = key[0]
        col_id = key[1]
        if self.items[row_id][col_id] > 0:
            self.items[row_id][col_id] -= 1

