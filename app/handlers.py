from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.gpt_generator import gpt_generator as gpt
from app.gemini_generator import gemini_generator as gemini
import app.keyboard as kb


router = Router()

class Question(StatesGroup):
    model = State()
    question = State()
    wait = State()


@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}\n\
                         Выбери модель для запроса!', reply_markup=kb.start_keyboard)

@router.callback_query(F.data == 'profile')
async def profile(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(f'Profile',
                                     reply_markup=kb.start_keyboard)

@router.callback_query(F.data.in_({'gpt', 'gemini'}))
async def choise(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(Question.model)
    if callback.data == 'gpt':
        await state.update_data(model='gpt')
        await state.set_state(Question.question)
        await callback.message.edit_text('Введите ваш запрос для GPT')
    else:
        await state.update_data(model='gemini')
        await state.set_state(Question.question)
        await callback.message.edit_text('Введите ваш запрос для Gemini')

@router.message(Question.question)
async def generator(message: Message, state: FSMContext):
    await state.update_data(question=message.text)
    data = await state.get_data()
    await state.set_state(Question.wait)
    if data['model'] == 'gpt':
        response = await gpt(data['question'])
    else:
        response = await gemini(data['question'])
    await state.clear()
    await message.answer(f'{response}', reply_markup=kb.start_keyboard)

@router.message(Question.wait)
async def generate_error(message: Message):
    await message.answer(f'Пожалуйста, подождите. Ваш ответ еще генерируется.')