from fastapi import Depends

from app.database import get_db
from app.advert.entities.advert_entity import AdvertEntity


class AdvertsPqRepository:
    def __init__(self, db = Depends(get_db)):
        self.db = db
    
    def create_advert(self, advert: AdvertEntity):
        self.db.add(advert)
        self.db.commit()
        self.db.refresh(advert)
        
        return advert
    
    def read_adverts(self):
        return self.db.query(AdvertEntity).all()
    
    def delete_advert(self, slug: str):
        advert = self.find_by_slug(slug)
        
        if advert is not None:
            self.db.delete(advert)
            self.db.commit()
    
    def find_by_slug(self, slug: str):
        return self.db.query(AdvertEntity).filter(AdvertEntity.slug == slug).first()
    
    def update_advert(self, advert: AdvertEntity):
        self.db.commit()
        self.db.refresh(advert)
        
        return advert