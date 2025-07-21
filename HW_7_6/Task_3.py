import aiohttp
import asyncio
import json


async def fetch_json(url):
    session = aiohttp.ClientSession()
    async with session:
            try:
                async with session.get(url) as resp:
                    data = await resp.json()
                    print(data)
            except aiohttp.ClientError:
                print(f"Ошибка при запросе {url}")


async def read_pages():
    tasks = []
    adresses = ["https://sovcombank.ru/solutions/insurance/avtozaschita", "https://httpbin.org/json",
                "https://api.github.com", "https://www.myjsons.com/", "https://example.com","https://mail.ru"]
    for url in adresses:
        task = asyncio.create_task(fetch_json(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(read_pages())