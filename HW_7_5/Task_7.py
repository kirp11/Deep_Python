import random
import asyncio

async def delayed_square(x):
    delay = random.randint(1,5)
    await asyncio.sleep(delay)
    print(f"{x*x}   c задержкой {delay} сек ")

tasks = []

async def paralel_sum(numb):
    sum_ = 0
    for num in numb:
        task = asyncio.create_task(delayed_square(num))
        tasks.append(task)
        sum_+= num*num
    await asyncio.gather(*tasks)
    print(f"Сумма квадратов равна {sum_}")



numbers = [random.randint(1,8) for i in range(10)]

print(numbers)

asyncio.run(paralel_sum(numbers))
