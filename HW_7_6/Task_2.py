
import aiohttp
import asyncio
dict_lens = {}

async def fetch_text(url):
    session = aiohttp.ClientSession()
    async with session:
        async with session.get(url) as resp:
            text = await resp.text()
            dict_lens[url] = f"Количество символов: {len(text)}"
            print(f"сайт по адресу : {url}  - статус {resp.status}   текст:  {text}")


async def read_pages():
    tasks = []
    adresses = ["https://dzen.ru/topic/multiki", "https://sovcombank.ru/solutions/insurance/avtozaschita", "https://ya.ru", "https://example.com","https://mail.ru", "https://github.com/kirp11/Snake_game/blob/main/README.md"]
    for url in adresses:
        task = asyncio.create_task(fetch_text(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(dict_lens)

asyncio.run(read_pages())