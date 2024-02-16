from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db",
    echo=True
)

new_session = async_sessionmaker(engine, expire_on_commit=False)  # expire_on_commit - разбирается в курсе по алхимии


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    """Описание таблицы"""
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


async def create_tables():
    """АСИНХРОННАЯ Функция для создания таблицы"""
    async with engine.begin() as connection:
        await connection.run_sync(Model.metadata.create_all)


async def delete_tables():
    """АСИНХРОННАЯ Функция для удаления таблицы"""
    async with engine.begin() as connection:
        await connection.run_sync(Model.metadata.drop_all)
