import asyncio
from bot import bot, dp
from aiogram.types import Message


@dp.message_handler(commands=["start"])
async def start(message: Message):
    await message.reply(f'Hi!')


async def main(dp):

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main(dp))

