from aiogram import Router
from aiogram.types import Message

import app.keyboards as kb
from app.database.requests import set_admin, get_reserve

router_admin = Router()


async def admin_menu(message: Message):
    admin = await set_admin(message.from_user.id)
    all_reserve = await get_reserve()
    
    await message.answer(f'Здравствуйте, {admin.name}!\n\nВот список записей:')
    
    # Проверяем, есть ли записи
    if not all_reserve:
        await message.answer("Нет записей.")
        return

    # Формируем текст для всех записей
    for reserve in all_reserve:
        message_text = (f'''Имя клиента: {reserve.user_name}, Номер клиента: {reserve.user_number}, Имя барбера: {reserve.barber_name}, Услуга: {reserve.service_name}\n''')
        await message.answer(message_text)