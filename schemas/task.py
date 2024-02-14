from pydantic import BaseModel
from typing import Union


class STaskAdd(BaseModel):
    name: str
    description: Union[str, None] = None

class STask(STaskAdd):
    id: int
