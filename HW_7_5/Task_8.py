import time

import asyncio

async def check(count):
    start = int(time.time())
    delay = 1
    while count > 0:

        await asyncio.sleep(delay)
        end = int(time.time())
        time_period = end - start
        if time_period % 5 == 0:
            print(f"ПРошедшее с начала времяя ({time_period}сек) ДЕЛИТСЯ на  5")
        else:
            print(f"ПРошедшее с начала времяя ({time_period}сек) НЕ делится на  5")
        count -=1




asyncio.run(check(10))