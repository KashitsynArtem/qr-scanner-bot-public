import logging
import asyncio
import filters
import handlers
from bot import bot, dp
from aiogram import Dispatcher


logging.basicConfig(level=logging.INFO)


async def main(dp: Dispatcher) -> None:
    filters.setup(dp)
    handlers.setup(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main(dp))

