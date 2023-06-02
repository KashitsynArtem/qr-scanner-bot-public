from .admin import register_admin
from aiogram import Dispatcher


def setup(dp: Dispatcher):
    register_admin(dp)






