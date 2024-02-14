from pydantic import BaseModel
from typing import Union


class Task(BaseModel):
    name: str
    description: Union[str, None] = None
