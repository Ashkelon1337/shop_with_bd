import os
import logging
from contextlib import asynccontextmanager
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Update
from fastapi import FastAPI, Request
import uvicorn
from config import TOKEN
from handlers import user, basket
from database.models import create_db

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    dp.include_router(user.router)
    dp.include_router(basket.router)
    webhook_url = os.getenv('RENDER_EXTERNAL_URL')
    if webhook_url:
        await bot.set_webhook(
            url=f'{webhook_url}/webhook',
            allowed_updates=dp.resolve_used_update_types(),
            drop_pending_updates=True
        )
        logging.info(f"✅ Webhook установлен на {webhook_url}/webhook")
    yield
    await bot.delete_webhook()
    logging.info("🔁 Webhook удалён")


app = FastAPI(lifespan=lifespan)

@app.post('/webhook')
async def webhook(request: Request):
    update_data = await request.json()
    update = Update.model_validate(update_data, context={'bot': bot})
    await dp.feed_update(bot, update)

@app.get('/health')
async def health():
    return {"status": 'ok'}

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    port = int(os.getenv('PORT', 8000))
    uvicorn.run('run:app', host='0.0.0.0', port=port, reload=False)