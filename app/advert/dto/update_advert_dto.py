from typing import List, Optional
from pydantic import BaseModel


class UpdateAdvertDto(BaseModel):
    thumbnail: Optional[str] = None 
    title: Optional[str] = None 
    description: Optional[str] = None 
    price: Optional[float] = None 
    tags: Optional[List[str]] = None 