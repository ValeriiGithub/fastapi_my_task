from fastapi import FastAPI
from schemas.task import STask, STaskAdd


app = FastAPI()

tasks = []
@app.post("/tasks")
async def create_task(task: STaskAdd,
                      ):
    tasks.append(task)
    return {"ok": True,
            "task": task}


# @app.get("/tasks")
# async def get_tasks():
#     task = STask(name="Запиши эту задачу")
#     return {"data": task}
