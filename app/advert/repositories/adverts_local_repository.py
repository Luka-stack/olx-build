from typing import List

from app.advert.models.advert import Advert


class AdvertsLocalRepository():
    def __init__(self):
        pass
    
    def create_advert(self, advert) -> Advert:
        pass
    
    def read_adverts(self) -> List[Advert]:
        pass
    
    def delete_advert(self, slug) -> None:
        pass
    
    def find_by_slug(self, slug) -> Advert | None:
        pass
    
    def update_advert(self, advert) -> Advert:
        pass