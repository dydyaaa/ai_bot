from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Профиль', callback_data='profile')],
    [InlineKeyboardButton(text='Gemini', callback_data='gemini'),
     InlineKeyboardButton(text='GPT', callback_data='gpt')],
])