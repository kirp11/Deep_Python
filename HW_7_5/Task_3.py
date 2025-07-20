
import asyncio
import random

tasks = []

async def task(number):
    delay = random.randint(1,8)
    await asyncio.sleep(delay)
    print(f"Задача номер {number}, с задержкой {delay}")

async def main():
    for i in range(1,8):
        task_ = asyncio.create_task(task(i))
        tasks.append(task_)
    await asyncio.gather(*tasks)


asyncio.run(main())
