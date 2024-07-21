import datetime
from typing import List


class Advert():
    def __init__(self, 
        id: int, 
        slug: str, 
        thumbnail: str, 
        title: str,
        description: str,
        price: float,
        owner: str,
        tags: List[str],
        created_at: datetime.datetime,
        updated_at = datetime.datetime,
    ):
        self.id = id
        self.slug = slug
        self.thumbnail = thumbnail
        self.title = title
        self.description = description
        self.price = price
        self.owner = owner
        self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at