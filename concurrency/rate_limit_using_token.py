from threading import Thread, Lock, current_thread
from time import sleep, time
import datetime


class TokenManager(object):
    def __init__(self):
        self.MAX_TOKEN = 3
        self.available_tokens = 0
        self.lock = Lock()
        self.last_processed_time = time()

    def get_token(self):
        with self.lock:
            self.available_tokens += int(time() - self.last_processed_time)
            if self.available_tokens >= self.MAX_TOKEN:
                self.available_tokens = self.MAX_TOKEN
            if self.available_tokens == 0:
                sleep(1)
            else:
                self.available_tokens -= 1
            self.last_processed_time = time()
            print("Grating {} token at {}".format(current_thread().name,
                                                  datetime.datetime.fromtimestamp(self.last_processed_time).strftime('%Y-%m-%d %H:%M:%S')))


token_manager = TokenManager()
threads = []
for i in range(30):
    t = Thread(target=token_manager.get_token, name="Thread {}".format(i))
    threads.append(t)
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
