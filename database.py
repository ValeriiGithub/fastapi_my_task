from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db",
    echo=True
)

new_session = async_sessionmaker(engine, expire_on_commit=False)    # expire_on_commit - разбирается в курсе по алхимии


class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
