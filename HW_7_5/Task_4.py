import asyncio


async def countdown(n):
    tasks = []
    async def output(number):
        delay = number - 1
        value = n - number
        print(f"Число {value} запущено")
        await asyncio.sleep(delay)
        print(f"Число {value}, с задержкой {delay}")


    for i in range(1,n+1):
        task_ = asyncio.create_task(output(i))
        tasks.append(task_)
    await asyncio.gather(*tasks)


asyncio.run(countdown(8))