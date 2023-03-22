import asyncio
import logging

from aiogram import Dispatcher, Bot
from scrt import TG_API

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_API) # todo: turn into secrets
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())