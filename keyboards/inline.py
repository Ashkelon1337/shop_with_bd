from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import database.requests as rq


async def items():
    items = await rq.get_items()
    keyboard = InlineKeyboardBuilder()
    for item in items:
        keyboard.button(text=item.name, callback_data=f'item_{item.id}')
    return keyboard.adjust(2).as_markup()

caption_car = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад к каталогу', callback_data='return_to_catalog'),
     InlineKeyboardButton(text='➕ Добавить в корзину', callback_data='Add_to_basket')]
])