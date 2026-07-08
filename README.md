# 🚗 Car Shop Bot

A Telegram bot for selling cars, featuring an interactive catalog, shopping cart functionality, and database integration.

---

## 📌 Features

* **User Registration:** Automatically registers users upon initial interaction.
* **Product Catalog:** Fetches and displays available vehicles directly from the database.
* **Detailed Product Views:** Showcases vehicle specifications along with media/photos.
* **Shopping Cart with Quantity Selection:** Utilizes FSM (Finite State Machine) to handle seamless product additions and count selections.
* **Persistent Storage:** Keeps track of users' shopping carts directly inside an SQLite database.
* **Cart Summary:** Allows users to view their cart with an automatically calculated total price.

---

## 🛠 Tech Stack

* **Framework:** aiogram 3.x
* **Database & ORM:** SQLAlchemy + aiosqlite (Async SQLite)
* **State Management:** FSM (Finite State Machine)

---

## 🎮 Bot Commands & Navigation

* `/start` — Initializes the bot and registers the user.
* `🚗 Catalog` (Reply Button) — Opens the list of available vehicles.
* `🛒 Cart` (Reply Button) — Views the current shopping cart items and the total bill.

---

## 🚀 Installation & Setup

1. **Clone the repository:**
    git clone [https://github.com/Ashkelon1337/shop_with_bd.git](https://github.com/Ashkelon1337/shop_with_bd.git)
    cd shop_with_bd
2. **Create and activate a virtual environment:**
    #### On Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate
    
    #### On Windows
    python -m venv .venv
    .venv\Scripts\activate
3. **Install the required dependencies:**
    pip install -r requirements.txt
4. **Configure environment variables: Create a .env file in the root directory and add your Telegram Bot token:**
    BOT_TOKEN=your_bot_token_here
5. **Run the application:**
    python run.py
