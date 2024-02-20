from __future__ import annotations

from fastapi import APIRouter, Depends
from typing_extensions import Annotated     # импортируем Annotated для версий python3.8 и ниже

from repository import TaskRepository
from schemas.task import STaskAdd, STask, STaskId
from typing import List

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)
@router.post("")
async def create_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> List[STask]:
    tasks = await TaskRepository.get_all()
    return tasks
