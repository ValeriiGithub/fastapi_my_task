from pydantic import BaseModel
from typing import Union


class STask(BaseModel):
    name: str
    description: Union[str, None] = None
