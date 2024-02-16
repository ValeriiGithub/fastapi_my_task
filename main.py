# from typing import Annotated    # с версии python 3.9
from typing_extensions import Annotated

from fastapi import FastAPI, Depends
from schemas.task import STask, STaskAdd

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield


app = FastAPI(lifespan=lifespan)

tasks = []
@app.post("/tasks")
async def create_task(
        task: Annotated[STaskAdd, Depends()],
                      ):
    tasks.append(task)
    return {"ok": True}


# @app.get("/tasks")
# async def get_tasks():
#     task = STask(name="Запиши эту задачу")
#     return {"data": task}
