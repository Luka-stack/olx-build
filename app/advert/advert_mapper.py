from app.advert.models.advert import Advert
from app.advert.dto.advert_dto import AdvertDto


class AdvertMapper():
    @staticmethod
    def model_to_dto( model: Advert) -> AdvertDto:
        pass