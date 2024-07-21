from http import HTTPStatus
from fastapi import APIRouter, Depends

from app.advert.dto.advert_dto import AdvertDto
from app.advert.adverts_service import AdvertsService
from app.advert.dto.create_advert_dto import CreateAdvertDto
from app.advert.dto.update_advert_dto import UpdateAdvertDto

router = APIRouter(
    prefix="/adverts",
    tags=["adverts"],
)

@router.get("/{slug}", response_model=AdvertDto)
def read_advert(slug: str, advert_service: AdvertsService = Depends()):
    return advert_service.read_advert(slug)

@router.get("/", response_model=list[AdvertDto])
def read_all(advert_service: AdvertsService = Depends()):
    return advert_service.read_all_adverts()

@router.post(
    "/", 
    response_model=AdvertDto, 
    status_code=HTTPStatus.CREATED
)
def create_advert(advertDto: CreateAdvertDto, advert_service: AdvertsService = Depends()):
    return advert_service.create_advert(advertDto)

@router.patch("/{slug}", response_model=AdvertDto)
async def update_advert(slug: str, advertDto: UpdateAdvertDto, advert_service: AdvertsService = Depends()):
    return advert_service.update_advert(slug, advertDto)

@router.delete("/{slug}", status_code=HTTPStatus.NO_CONTENT)
def delete_advert(slug: str, advert_service: AdvertsService = Depends()):
    advert_service.delete_advert(slug)
