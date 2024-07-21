from typing import List
from pydantic import BaseModel


class CreateAdvertDto(BaseModel):
    thumbnail: str
    title: str
    description: str
    price: float
    owner: str
    tags: List[str]