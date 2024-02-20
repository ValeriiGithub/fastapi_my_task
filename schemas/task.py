from pydantic import BaseModel, ConfigDict
from typing import Union


class STaskAdd(BaseModel):
    name: str
    description: Union[str, None] = None

class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int

