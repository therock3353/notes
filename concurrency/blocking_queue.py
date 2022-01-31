from threading import Thread, Condition, current_thread
from time import sleep
from random import randint

class BlockingQueue(object):

    def __init__(self, size):
        self.size = size
        self.queue = []
        self.cond = Condition()

    def push(self, elem):
        with self.cond:
            while len(self.queue) >= self.size:
                print("Queue size full")
                self.cond.wait()
            self.queue.append(elem)
            print("Thread {} :adding element {} to queue".format(current_thread().name, elem))
            self.cond.notify_all()

    def pop(self):
        with self.cond:
            while not self.queue:
                print("Queue is empty")
                self.cond.wait()
            elem = self.queue.pop(0)
            print("Thread {} :removing element {} from queue".format(current_thread().name, elem))
            self.cond.notify_all()
            return elem


def producer(b_queue):
    i = 0
    while i < 10:
        b_queue.push(randint(1, 100))
        sleep(1)
        i += 1

def consumer(b_queue):
    while True:
        b_queue.pop()
        sleep(0.2)

queue = BlockingQueue(10)
prod_thread = Thread(target=producer, args=(queue, ))
prod_thread.start()
consumer_thread = Thread(target=consumer, args=(queue, ))
consumer_thread.start()


