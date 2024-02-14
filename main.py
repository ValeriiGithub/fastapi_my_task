from fastapi import FastAPI
from schemas.task import STask


app = FastAPI()


class


@app.get("/tasks")
async def get_tasks():
    task = STask(name="Запиши эту задачу")
    return {"data": task}
