import datetime
from typing import List
from pydantic import BaseModel


class AdvertDto(BaseModel):
    slug: str
    thumbnail: str
    title: str
    description: str
    price: float
    owner: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    tags: List[str]