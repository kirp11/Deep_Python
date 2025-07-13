import random
import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print(f"Поток {self.name} работает")
        time.sleep(random.randint(1,4))
        print(f"Поток {self.name} уснул")
threads = []

for i in range(1,9):
    th = MyThread()
    threads.append(th)

for thread in threads:
    thread.start()