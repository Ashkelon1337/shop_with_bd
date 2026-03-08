from aiogram import Bot, Dispatcher
from config import TOKEN
import logging, asyncio
from handlers import user, basket
from database.models import create_db

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await create_db()
    dp.include_router(user.router)
    dp.include_router(basket.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')