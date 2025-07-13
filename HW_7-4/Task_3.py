import random
import threading
import time

count = 0
threads = []
def change_count(i, delay):
    global count

    print(f"Поток {thread.name} включает увеличение счетчика через {delay} секунд")

    time.sleep(delay)
    count += 1

    print(f"После влияния потока {i} счетчик равен {count}")


for i in range(1,51):
    delay = random.randint(1, 8)
    th = threading.Thread(target=change_count, args=(i,delay))
    threads.append(th)

for thread in threads:

    thread.start()