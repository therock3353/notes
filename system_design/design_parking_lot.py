from datetime import datetime

class ParkingLot(object):
    def __init__(self):
        self.MAX_SMALL_PARKING_SPACES = 10
        self.MAX_LARGE_PARKING_SPACES = 5
        self.available_small_spaces = self.MAX_SMALL_PARKING_SPACES
        self.available_large_spaces = self.MAX_LARGE_PARKING_SPACES

    def is_space_available(self, car):
        if isinstance(car, SmallCar):
            if self.available_small_spaces > 0:
                return True
            else:
                return False
        elif isinstance(car, LargeCar):
            if self.available_large_spaces > 0:
                return True
            else:
                return False

    def decrease_available_parking_space(self, car):
        if isinstance(car, SmallCar):
            self.available_small_spaces -= 1
        elif isinstance(car, LargeCar):
            self.available_large_spaces -= 1

    def generate_ticket(self, car):
        ticket = Ticket(car)
        return ticket

    def checkin(self, car):
        if not self.is_space_available(car):
            return Exception("Parking space full")
        ticket = self.generate_ticket(car)
        car.checkin(ticket)

    def checkout(self, car):
        ticket = car.get_ticket()
        ticket.pay()
        car.checkout()

class Ticket(object):
    def __init__(self, car):
        self.checkin_time = datetime.now()
        self.checkout_time = None
        self.car_type = type(car)
        self.car_payment_processor = self.get_payment_processor(car)
        self.payment_calc = PaymentCalculator()

    def get_payment_processor(self, car):
        if isinstance(car, SmallCar):
            return SmallCarPaymentProcessor()
        elif isinstance(car, LargeCar):
            return LargeCarPaymentProcessor()

    def get_total_time(self):
        pass

    def pay(self):
        self.payment_calc.calculate_payment()

class Car(object):
    def __init__(self, id):
        self.id = id
        self.ticket = None
        self.state = None

    def checkin(self, ticket):
        self.ticket = ticket
        self.state = "PARKED"

    def checkout(self):
        self.ticket = None
        self.state = None

class SmallCar(Car):
    def __init__(self, id):
        self.payment_processor = SmallCarPaymentProcessor()
        super(SmallCar, self).__init__(id)

class LargeCar(Car):
    def __init__(self, id):
        self.payment_processor = LargeCarPaymentProcessor()
        super(LargeCar, self).__init__(id)

class SmallCarPaymentProcessor(object):
    def __init__(self):
        self.hr_rate = "10"
        self.full_day_rate = "40"

    def process_payment(self, total_time):
        if total_time < 60:
            return 10
        elif 60 < total_time < 120:
            return 20
        else:
            return 40

class LargeCarPaymentProcessor(object):
    def __init__(self):
        self.hr_rate = "30"
        self.full_day_rate = "120"

    def process_payment(self, total_time):
        if total_time < 60:
            return 30
        elif 60 < total_time < 120:
            return 60
        else:
            return 120

class PaymentCalculator(object):
    def get_corp_discount(self):
        return 0

    def make_daily_adjustment(self):
        return 0

    def calculate_payment(self, payment_processor):
        final_cost = self.get_corp_discount() + self.make_daily_adjustment() + \
                     payment_processor.process_payment()
        return final_cost