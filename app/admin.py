from aiogram import Router
from aiogram.types import Message

import app.keyboards as kb
from app.database.requests import set_admin

router_admin = Router()


async def admin_menu(message: Message):

    admin = await set_admin(message.from_user.id)

    await message.answer(f'Здравствуйте, {admin.name}!')
    await message.answer('Вот список записей:')

