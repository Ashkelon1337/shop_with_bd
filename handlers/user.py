
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import database.requests as rq
from aiogram.fsm.state import State, StatesGroup
import keyboards.inline as inl
from keyboards import inline

router = Router()

class Add_to_basket(StatesGroup):
    waiting_for_quantity = State()

@router.message(CommandStart())
async def comstart(message: Message):
    from keyboards import reply
    print(f"🚀 /start от {message.from_user.id}")
    await rq.create_user(message.from_user.id)
    print("✅ create_user выполнен")
    await message.answer(
        f'🚗 Привет, {message.from_user.first_name}!\n \n'
        'Я бот магазин крутых тачек. Здесь ты можешь:\n'
        '• Посмотреть каталог автомобилей\n'
        '• Добавить машину в корзину\n'
        '• Оформить заказ\n\n'
        'Используй кнопки внизу 👇', reply_markup=reply.command_start
    )
@router.message(F.text == '🚗 Каталог')
async def Catalog(message: Message):
    await message.answer(text='🚗 Наши автомобили:', reply_markup= await inl.items())

@router.callback_query(F.data.startswith('item_'))
async def show_car(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    item_id = int(callback.data.split('_')[1])
    await state.update_data(current_item_id=item_id)
    item = await rq.get_item_by_id(item_id)
    await callback.message.answer_photo(photo=item.photo, caption=f'🚗 {item.name}\n\n{item.description}\n{item.price}Р', reply_markup=inline.caption_car)



@router.callback_query(F.data == 'return_to_catalog')
async def return_to_catalog(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text='🚗 Наши автомобили:', reply_markup= await inl.items())
@router.message(F.text == '📞 Контакты')
async def contacts(message: Message):
    text = """
    📞 **Наши контакты:**

    Email: danilashakirov33@gmail.com
    Адрес: Россия

    📱 Telegram: @Ashkelon1337
    
    Режим работы: Круглосуточно
        """
    await message.answer(text)