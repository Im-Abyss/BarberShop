from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

router_admin = Router()

class Admin(StatesGroup):
    owner = State()


async def admin_menu(message: Message, state: FSMContext, admin):
    await message.answer(f'Здравствуйте, {admin.name}!')
    await message.answer('Вот список ваших клиентов.', reply_markup=await kb.clients())
    await state.set_state(Admin.owner)