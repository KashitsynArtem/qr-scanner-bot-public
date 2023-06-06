import logging
import asyncio
import filters
import handlers
from bot import bot, dp
from aiogram import Dispatcher
import os


logging.basicConfig(level=logging.INFO)


async def main(dispatcher: Dispatcher) -> None:
    filters.setup(dispatcher)
    handlers.setup(dispatcher)

    try:
        await dispatcher.start_polling()
    finally:
        await dispatcher.storage.close()
        await dispatcher.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main(dp))

