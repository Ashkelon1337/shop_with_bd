from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

command_start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🚗 Каталог')],
    [KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="📞 Контакты")],
], resize_keyboard=True)