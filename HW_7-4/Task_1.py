
import threading
import time
import random

threads = []
def output(num):

    time_delay = random.randint(1,4)
    print(f"Поток {num} запущен, мое время сна {time_delay} сек")

    time.sleep(time_delay)
    print(f"Привет из потока {num}")




for i in range(1, 9):
    thread = threading.Thread(target=output, args={i})
    threads.append(thread)

for th in threads:
    th.start()

