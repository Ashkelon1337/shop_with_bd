from database.models import async_session
from database.models import User, Items, Basket
from sqlalchemy import select

async def get_items():
    async with async_session() as session:
        items = await session.scalars(select(Items))
        return items.all()

async def get_item_by_id(item_id):
    async with async_session() as session:
        item = await session.scalar(select(Items).where(Items.id == item_id))
        return item

async def get_user_id(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user

async def create_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def add_to_basket(user_id, item_id, quantity):
    async with async_session() as session:
        item = await session.scalar(select(Basket).where(Basket.user_id == user_id, Basket.item_id == item_id))
        if not item:
            session.add(Basket(user_id=user_id, item_id=item_id, quantity=quantity))
            await session.commit()
        else:
            item.quantity = item.quantity + quantity
            await session.commit()
async def get_basket(user_id):
    async with async_session() as session:
        basket = await session.scalars(select(Basket).where(Basket.user_id == user_id))
        return basket.all()

async def remove_from_basket(user_id, item_id):
    async with async_session() as session:
        item = await session.scalar(select(Basket).where(Basket.user_id == user_id, Basket.item_id == item_id))
        await session.delete(item)
        await session.commit()

async def clear_basket(user_id):
    async with async_session() as session:
        items = await session.scalars(select(Basket).where(Basket.user_id == user_id))
        for item in items:
            session.delete(item)
        await session.commit()