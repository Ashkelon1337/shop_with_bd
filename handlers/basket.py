from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import database.requests as rq

router = Router()
class Add_to_basket(StatesGroup):
    quantity = State()
@router.callback_query(F.data == 'Add_to_basket')
async def Add_start(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    car_id = data.get('current_item_id')
    if car_id is None:
        await callback.answer("Ошибка! Выберите машину заново")
        return
    await state.set_state(Add_to_basket.quantity)
    await callback.message.answer('Сколько штук добавить?')
    await callback.answer()

@router.message(Add_to_basket.quantity)
async def add_quantity(message: Message, state : FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите число!")
        return

    quantity = int(message.text)
    user = await rq.get_user_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start")
        await state.clear()
        return
    data = await state.get_data()
    item_id = data.get('current_item_id')
    await rq.add_to_basket(user.id, item_id, quantity)
    await state.clear()
    await message.answer(f"✅ Добавлено {quantity} шт.")
@router.message(F.text == '🛒 Корзина')
async def show_basket(message: Message):
    user = await rq.get_user_id(message.from_user.id)
    basket = await rq.get_basket(user.id)

    text = '🛒 **Твоя корзина:**\n\n'
    total = 0
    for item in basket:
        car = await rq.get_item_by_id(item.item_id)
        price = car.price
        name_car = car.name
        quantity = item.quantity
        text += f'• {name_car} в количестве {quantity} = {price * quantity}\n'
        total += price * quantity

    text += f'\nИтого: {total}'
    await message.answer(text)
