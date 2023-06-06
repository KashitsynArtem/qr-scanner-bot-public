from aiogram import Dispatcher
from aiogram.types import Message, InputFile
from qr_base.qr_base import qr_scan, qr_gen
from bot import bot
from io import BytesIO


async def start(message: Message) -> None:
    await message.answer(text='Hello, Im a QR bot, thats what I can do:\n\n\n'
                              '• Send your message or link to the bot, and it will create a unique QR code\n\n'
                              '• Send a image or photo with QR code or barcode to the bot, and it will instantly '
                              'decode the information and display it for you.')
    await message.delete()


async def read_qr(message: Message) -> None:
    buf = BytesIO()
    await message.photo[-1].download(destination_file=buf)
    res = await qr_scan(buf)

    if res:
        await bot.send_message(message.from_user.id, text=f'On QR: {res}')
    else:
        await bot.send_message(message.from_user.id, text=f'Image without QR')


async def get_qr(message: Message) -> None:
    user_id: int = message.from_user.id
    msg_text: str = message.text
    buf = await qr_gen(msg_text)
    await bot.send_photo(user_id,
                         caption=f'On QR: {msg_text}',
                         photo=InputFile(buf, f'{str(user_id)}.png'))


def register_admin(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"], is_admin=True)
    dp.register_message_handler(read_qr, content_types=['photo'], is_admin=True)
    dp.register_message_handler(get_qr, content_types=['text'], is_admin=True)
