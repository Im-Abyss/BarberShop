from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
from app.database.requests import only_admin_name

router_admin = Router()


async def admin_menu(message: Message):

    admin_name = await only_admin_name(message.from_user.id)

    await message.answer(f'Здравствуйте, {admin_name}!')
    await message.answer('Вот список ваших клиентов.', reply_markup=await kb.clients())

