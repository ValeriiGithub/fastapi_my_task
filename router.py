from __future__ import annotations

from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from repository import TaskRepository
from schemas.task import STaskAdd, STask

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)
@router.post("")
async def create_task(
        task: Annotated[STaskAdd, Depends()],
                      ):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True,
            "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return tasks
