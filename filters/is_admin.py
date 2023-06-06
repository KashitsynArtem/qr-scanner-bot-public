import os
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: bool):
        self.is_admin = is_admin

    async def check(self, message: types.Message) -> bool:
        if id_admin := os.environ.get('ID_ADMIN'):
            return int(message.from_user.id) == int(id_admin)
        return True










