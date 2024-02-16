from __future__ import annotations
from sqlalchemy import select

from database import new_session, TaskOrm
from schemas.task import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()       # приводим data к виду dict

            task = TaskOrm(**task_dict)

            # Блок добавления task в БД
            session.add(task)                   # эта операция синхронная т.к. к БД еще не обращаемся
            await session.flush()               # еще не завершает транзакцию (добавление строки), отправит изменения
                                                # в БД и получит id при автоинкременте
                                                # т.о. поле id будет зафиксировано, и мы сможем его вернуть
            await session.commit()              # сессия отправляется в БД со сделанными изменениями через коммит
            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)                 # запрос
            result = await session.execute(query)   # исполнить запрос
            task_models = result.scalars().all()    # объекты алхимии, к-е вернуться
            # конвертация к pydantic схемам
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_models
