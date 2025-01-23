from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_barbers, get_services, get_clients

contact = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отправить контакт', request_contact=True)]
], resize_keyboard=True, input_field_placeholder='Нажмите кнопку ниже.')


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Записаться на услугу')],
    [KeyboardButton(text='Контакты/локация')]
], resize_keyboard=True)


async def barbers():
    all_barbers = await get_barbers()
    keyboard = InlineKeyboardBuilder()
    for barber in all_barbers:
        keyboard.add(InlineKeyboardButton(text=barber.name, callback_data=f'barber_{barber.id}'))
    return keyboard.adjust(1).as_markup()


async def services():
    all_services = await get_services()
    keyboard = InlineKeyboardBuilder()
    for service in all_services:
        keyboard.add(InlineKeyboardButton(text=service.name, callback_data=f'service_{service.id}'))
    return keyboard.adjust(1).as_markup()


async def clients():
    all_clients = await get_clients()
    keyboard = InlineKeyboardBuilder()
    for client in all_clients:
        keyboard.add(InlineKeyboardButton(text=client.name, callback_data=f'client_{client.id}'))
    return keyboard.adjust(1).as_markup()