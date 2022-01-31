from threading import Thread, current_thread
from time import sleep
import random
from queue import Queue

#In python Queue is thread-safe

class Producer(object):
    def __init__(self):
        self.queue = Queue(maxsize=2)

    def produce(self):
        i = 0
        while i < 10:
            num = random.randint(1, 100)
            self.queue.put(num)
            print("{} produced {}".format(current_thread().name, num))
            i += 1
            sleep(0.1)

class Consumer(object):
    def __init__(self, prod):
        self.producer = prod

    def consume(self):
        while self.producer.queue:
            num = self.producer.queue.get()
            print("{} consumed {}".format(current_thread().name, num))
            sleep(0.5)

producer = Producer()
consumer = Consumer(producer)
prod_thread = Thread(target=producer.produce, name="Producer Thread")
consumer_thread = Thread(target=consumer.consume, name="Consumer Thread")
prod_thread.start()
consumer_thread.start()

prod_thread.join()
consumer_thread.join()
