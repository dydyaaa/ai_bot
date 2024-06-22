from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboard as kb


router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name}', reply_markup=kb.start_keyboard)

@router.callback_query(F.data == 'profile')
async def profile(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Profile')