# импорты
import aiohttp
import asyncio

# создаем асинхронную функцию
async def func():
    async with aiohttp.ClientSession() as session: # открытие сессии в aiohttp
        response = await session.get("http://localhost:8000/123", params={"user": "PoliHas"}) # отправка запроса

        print(response)
        res = await response.text()
        print(res)
 
asyncio.run(func())       
# loop = asyncio.new_event_loop() # создаём новый асинхронный цикл
# loop.create_task(func()) # добавляем в него нашу функцию 
# loop.run_forever() # запускаем цикл

