from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db_sqlite3')
async_session = async_sessionmaker(engine)

class Base(DeclarativeBase, AsyncAttrs):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger, unique=True)

class Items(Base):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(69))
    description: Mapped[str] = mapped_column(String(125))
    photo: Mapped[str] = mapped_column(String(225))
    price: Mapped[int] = mapped_column()

class Basket(Base):
    __tablename__ = "basket"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))
    quantity: Mapped[int] = mapped_column()

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
