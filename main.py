from fastapi import FastAPI
from schemas.task import Task


app = FastAPI()


@app.get("/tasks")
async def get_tasks():
    task = Task(name="Запиши эту задачу")
    return {"data": task}
