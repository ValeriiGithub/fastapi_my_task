from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from repository import TaskRepository
from schemas.task import STaskAdd

router = APIRouter(
    prefix="/tasks"
)
@router.post("")
async def create_task(
        task: Annotated[STaskAdd, Depends()],
                      ):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True,
            "task_id": task_id}


# @router.get("")
# async def get_tasks():
#     task = STask(name="Запиши эту задачу")
#     return {"data": task}