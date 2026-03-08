# 🚗 Car Shop Bot

Telegram-бот для продажи автомобилей с каталогом, корзиной и базой данных.

## 📌 Возможности
- ✅ Регистрация пользователей
- ✅ Просмотр каталога товаров (из БД)
- ✅ Детальная информация о товаре с фото
- ✅ Добавление в корзину с выбором количества (FSM)
- ✅ Хранение корзины в базе данных SQLite
- ✅ Просмотр корзины с подсчётом итоговой суммы

## 🛠 Технологии
- Aiogram 3.x
- SQLAlchemy + aiosqlite
- FSM (Finite State Machine)
- 
## Команды
- "/start" - Начало работы
- Кнопка "🚗 Каталог" - список машин
- Кнопка "🛒 Корзина" - просмотр корзины

## 🚀 Установка и запуск
1. **Клонируй репозиторий**
   bash
   git clone https://github.com/Ashkelon1337/shop_with_bd.git
   cd shop_with_bd
2. Создай виртуальное окружение
  python -m venv .venv
  source .venv/bin/activate  # для Linux/Mac
  .venv\Scripts\activate     # для Windows
3. Установи зависимости
  pip install -r requirements.txt
4. Создай файл .env и добавь токен бота:
  BOT_TOKEN=твой_токен_сюда
5. Запусти бота
  python run.py
