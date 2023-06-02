import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv()
bot = Bot(token=os.environ.get('BOT_API_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())


