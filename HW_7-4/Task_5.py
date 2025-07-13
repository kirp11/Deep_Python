
import threading
import time
import random

threads = []
lst_value = []
mutex = threading.Lock()
def add_element(num, value):
    print(f"Вносятся изменения от потока {num}")
    mutex.acquire()

    time.sleep(random.randint(1,8))
    lst_value.append(value)

    mutex.release()
    print(f"Изменения от потока  {num} добавлены, измененный список: {lst_value}")




for i in range(1, 4):
    thread = threading.Thread(target=add_element, args=(i,[(random.randint(1,100)) for i in range(5)]))
    threads.append(thread)

for th in threads:
    th.start()