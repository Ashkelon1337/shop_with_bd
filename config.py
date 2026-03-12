import os
from dotenv import load_dotenv

load_dotenv()

# Токен бота
TOKEN = os.getenv("BOT_TOKEN")

# Строка подключения к базе (Render подставит целиком)
DATABASE_URL = os.getenv("DATABASE_URL")

# Если есть Google Sheets
GOOGLE_CREDS = os.getenv("GOOGLE_CREDS")  # если используешь

# Проверка (для отладки)
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не задан!")
if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL не задан! Забыл добавить переменную на Render?")