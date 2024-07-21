from typing import List


class CreateAdvertDto():
    thumbnail: str
    title: str
    description: str
    price: float
    owner: str
    tags: List[str]