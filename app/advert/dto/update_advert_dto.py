from typing import List, Optional


class UpdateAdvertDto():
    thumbnail: Optional[str] = None 
    title: Optional[str] = None 
    description: Optional[str] = None 
    price: Optional[float] = None 
    tags: Optional[List[str]] = None 