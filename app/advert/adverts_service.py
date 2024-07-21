import datetime
import logging
from http import HTTPStatus
from fastapi import Depends, HTTPException

from app.advert.adverts_pq_repository import AdvertsPqRepository
from app.advert.dto.create_advert_dto import CreateAdvertDto
from app.advert.dto.update_advert_dto import UpdateAdvertDto
from app.advert.entities.advert_entity import AdvertEntity


class AdvertsService:
    def __init__(self, repo: AdvertsPqRepository = Depends()):
        print('AdvertsService')
        
        logging.info("Advert service initialized")
        self.repo = repo

    def create_advert(self, advertDto: CreateAdvertDto):
        logging.info("Creating advert")
        
        advert = AdvertEntity(
            slug = self._create_slug(advertDto.title),
            thumbnail = advertDto.thumbnail,
            title = advertDto.title,
            description = advertDto.description,
            price = advertDto.price,
            owner = advertDto.owner,
            tags = advertDto.tags
        )
        
        try:
            return self.repo.create_advert(advert)
        except:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Advert title must be unique"
            )

    def read_advert(self, slug: str):
        logging.info("Reading " + slug)
        
        advert = self.repo.find_by_slug(slug)
        
        if advert is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Advert not found")
        
        return advert

    def update_advert(self, slug: str, advertDto: UpdateAdvertDto):
        logging.info("Updating " + slug)
        
        db_advert = self.repo.find_by_slug(slug)
        
        if db_advert is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Advert not found")
        
        updated_advert = self._update_fields(db_advert, advertDto)
        
        try:
            return self.repo.update_advert(updated_advert)
        except:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Advert title must be unique"
            )

    def delete_advert(self, slug: str):
        logging.info("Deleting " + slug)
        
        self.repo.delete_advert(slug)
        
    def read_all_adverts(self):
        logging.info("Readling all adverts")
        
        return self.repo.read_adverts()
    
    def _create_slug(self, title: str):
        return title.lower().replace(" ", "-")

    def _update_fields(self, advert, advertDto):
        advert.thumbnail = advertDto.thumbnail if advertDto.thumbnail is not None else advert.thumbnail
        advert.title = advertDto.title if advertDto.title is not None else advert.title
        advert.description = advertDto.description if advertDto.description is not None else advert.description
        advert.price = advertDto.price if advertDto.price is not None else advert.price
        advert.tags = advertDto.tags if advertDto.tags is not None else advert.tags
        advert.updated_at = datetime.datetime.now()
        
        if advertDto.title is not None:
            advert.slug = self._create_slug(advertDto.title)
        
        
        return advert