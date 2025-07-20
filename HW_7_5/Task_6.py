
import aiohttp
import asyncio

adresses = ["https://ya.ru","https://example.com","https://mail.ru", "https://github.com/kirp11/Snake_game/blob/main/README.md"]

async def f():
    async with  aiohttp.ClientSession(trust_env = True) as session:
        for url in adresses:
            async with session.get(url) as response:
                print(response.status)

asyncio.run(f())
