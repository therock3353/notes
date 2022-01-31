from threading import Thread, Condition, current_thread
from time import sleep
import random

class Producer(object):
    def __init__(self):
        self.queue = []
        self.MAX_NUM = 2
        self.condition = Condition()

    def produce(self):
        i = 0
        while i < 10:
            #global condition
            with self.condition:
                while len(self.queue) >= self.MAX_NUM:
                    print("{} waiting for Queue size to shrink from {}".format(current_thread().name, len(self.queue)))
                    self.condition.wait()
                num = random.randint(1, 1000)
                self.queue.append(num)
                print("{} produced {}".format(current_thread().name, num))
                i += 1
                self.condition.notify_all()
                sleep(0.1)

class Consumer(object):
    def __init__(self, prod):
        self.producer = prod

    def consume(self):
        i = 0
        while i < 10:
            # global condition
            with self.producer.condition:
                while not self.producer.queue:
                    print("Queue is empty hence {} waiting".format(current_thread().name))
                    self.producer.condition.wait()
                num = self.producer.queue.pop(0)
                print("{} consumed {}".format(current_thread().name, num))
                i += 1
                self.producer.condition.notify_all()
                sleep(0.5)

producer = Producer()
consumer = Consumer(producer)
prod_thread = Thread(target=producer.produce, name="Producer Thread")
consumer_thread = Thread(target=consumer.consume, name="Consumer Thread")
prod_thread.start()
consumer_thread.start()

prod_thread.join()
consumer_thread.join()
