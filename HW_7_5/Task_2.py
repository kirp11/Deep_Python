
import asyncio

async def delayed_print(text, delay):
    await asyncio.sleep(delay)
    print(text)

asyncio.run(delayed_print("Привет", 2))
asyncio.run(delayed_print("Пока", 4))
asyncio.run(delayed_print("Нет", 6))