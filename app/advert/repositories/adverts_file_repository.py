from typing import List

from app.advert.models.advert import Advert


class AdvertsFileRepository():
    def __init__(self):
        pass
    
    def create_advert(self, advert: Advert) -> Advert:
        pass
    
    def read_adverts(self) -> List[Advert]:
        pass
    
    def delete_advert(self, slug: str) -> None:
        pass
    
    def find_by_slug(self, slug: str) -> Advert | None:
        pass
    
    def update_advert(self, slug: str, advert: Advert) -> Advert:
        pass