import aiohttp
import asyncio

async def fetch_status(url):
    session = aiohttp.ClientSession()
    async with session:
        async with session.get(url) as response:
            print(f"сайт по адресу : {url}  - статус {response.status}")



async def script():
    tasks = []
    adresses = ["https://example.com", "https://httpbin.org/status/404", "https://httpbin.org/status/500", "https://ya.ru", "https://example.com","https://mail.ru", "https://github.com/kirp11/Snake_game/blob/main/README.md"]
    for url in adresses:
        task = asyncio.create_task(fetch_status(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(script())