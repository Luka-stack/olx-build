from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException

from app.advert.advert_validator import AdvertValidator
from app.advert.adverts_service import AdvertsService

router = APIRouter(
    prefix="/adverts",
    tags=["adverts"],
)

@router.get("/{slug}")
def read_advert(slug: str, advert_service: AdvertsService = Depends()):
    return advert_service.read_advert(slug)

@router.get("/")
def read_all(advert_service: AdvertsService = Depends()):
    return advert_service.read_all_adverts()

@router.post(
    "/", 
    status_code=HTTPStatus.CREATED
)
def create_advert(advertDto: dict, advert_service: AdvertsService = Depends()):
    result = AdvertValidator.validate_create_advert(advertDto)
    
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Invalid advert data"
        )
    
    return advert_service.create_advert(advertDto)

@router.patch("/{slug}")
async def update_advert(slug: str, advertDto: dict, advert_service: AdvertsService = Depends()):
    result = AdvertValidator.validate_create_advert(advertDto)
    
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Invalid advert data"
        )
    
    return advert_service.update_advert(slug, advertDto)

@router.delete("/{slug}", status_code=HTTPStatus.NO_CONTENT)
def delete_advert(slug: str, advert_service: AdvertsService = Depends()):
    advert_service.delete_advert(slug)
