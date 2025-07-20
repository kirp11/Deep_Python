
import asyncio
async def say_hello():
    await asyncio.sleep(5)
    print("Привет!")

asyncio.run(say_hello())