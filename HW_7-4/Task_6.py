import random
import threading

massiv = [(random.randint(0,100)) for i in range(100)]
partial_sums = []
index = 0
threads = []


def calculate_sum(start, end, ind):

    local_sum = sum(massiv[k] for k in range(start, end))
    print(f"Сумма в потоке {ind} равна {local_sum}")
    partial_sums.insert(ind, local_sum)



for j in range(0, len(massiv), 5):

    th = threading.Thread(target=calculate_sum, args=(j, j+5, index))
    index += 1
    threads.append(th)


for thread in threads:
    thread.start()
    thread.join()


summ_massive = sum(partial_sums)


print(f"изначальный массив  {massiv}")
print(f"Сумма элементов в массиве {summ_massive}")
print(f" сам массив {partial_sums}")
print(f"проверка {sum(massiv)}")
