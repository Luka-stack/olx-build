import logging
from typing import List
from fastapi import Depends 

from app.advert.dto.advert_dto import AdvertDto
from app.advert.repositories.adverts_local_repository import AdvertsLocalRepository


class AdvertsService:
    def __init__(self, repo: AdvertsLocalRepository = Depends()):
        logging.info("Advert service initialized")
        self.repo = repo

    def create_advert(self, advertDto: dict) -> AdvertDto:
        logging.info("Creating advert")
        pass

    def read_advert(self, slug: str) -> AdvertDto:
        logging.info("Reading " + slug)
        pass

    def update_advert(self, slug: str, advertDto: dict) -> AdvertDto:
        logging.info("Updating " + slug)
        pass

    def delete_advert(self, slug: str) -> None:
        logging.info("Deleting " + slug)
        pass
        
    def read_all_adverts(self) -> List[AdvertDto]:
        logging.info("Readling all adverts")
        pass