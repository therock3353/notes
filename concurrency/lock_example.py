from threading import Thread, get_ident, Lock, current_thread
from random import randint
import time


class Asset(object):
    def __init__(self):
        self.i = 0
        self.lock = Lock()

    def change_variable(self, new_val):
        print("Thread {} ==> i changed from {} to {}".format(current_thread().name, self.i, new_val))
        self.i = new_val

    def process(self, new_val):
        self.lock.acquire()
        self.change_variable(new_val)
        self.lock.release()


def num_generator(asset):
    i = 0
    while i < 3:
        asset.process(randint(1, 1000))
        time.sleep(0.2)
        i += 1


if __name__ == "__main__":
    asset = Asset()
    t1 = Thread(target=num_generator, args=(asset,), name="Thread1")
    t1.start()
    t2 = Thread(target=num_generator, args=(asset,), name="Thread2")
    t2.start()
    t3 = Thread(target=num_generator, args=(asset,), name="Thread3")
    t3.start()

    t1.join()
    t2.join()
    t3.join()
