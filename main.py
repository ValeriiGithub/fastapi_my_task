# from typing import Annotated    # с версии python 3.9

from fastapi import FastAPI

from database import delete_tables, create_tables
from router import router as tasks_router

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    После запуска приложения:
    1 таблицы удаляются
    2 таблицы создаются
    :param app:
    :return:
    """
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База создана")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)


