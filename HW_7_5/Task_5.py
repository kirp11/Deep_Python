import asyncio
import random


async def fetch_data(index):
    tasks = []
    async def output():
        delay = random.randint(1,5)
        await asyncio.sleep(delay)
        print(f"Данные {index} получены ({delay} сек)")


    for i in range(5):
        task_ = asyncio.create_task(output())
        tasks.append(task_)
    await asyncio.gather(*tasks)


asyncio.run(fetch_data(5))