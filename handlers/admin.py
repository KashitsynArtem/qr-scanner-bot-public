from aiogram import Dispatcher
from aiogram.types import Message, InputFile
from qr_base.qr_base import qr_scan, qr_gen
from bot import bot
from io import BytesIO


async def start(message: Message) -> None:
    await message.answer(text='Hi')
    await message.delete()


async def read_qr(message: Message) -> None:
    buf = BytesIO()
    await message.photo[-1].download(destination_file=buf)
    res = await qr_scan(buf)

    if res:
        await bot.send_message(message.from_user.id, text=f'{res}')
    else:
        await bot.send_message(message.from_user.id, text=f'Nope')


async def get_qr(message: Message) -> None:
    user_id: int = message.from_user.id
    buf = await qr_gen(message.text)
    await bot.send_photo(user_id,
                         caption=f'QR:',
                         photo=InputFile(buf, f'{str(user_id)}.png'))


def register_admin(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"], is_admin=True)
    dp.register_message_handler(read_qr, content_types=['photo'], is_admin=True)
    dp.register_message_handler(get_qr, content_types=['text'], is_admin=True)
