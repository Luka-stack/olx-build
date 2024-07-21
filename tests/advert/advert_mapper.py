import datetime

from app.advert.models.advert import Advert
from app.advert.dto.advert_dto import AdvertDto
from app.advert.advert_mapper import AdvertMapper


def test_model_to_dto():
    advert = Advert(
        id=1,
        title="Title",
        description="Description",
        price=100.0,
        slug="title",
        owner="owner",
        thumbnail="thumbnail",
        tags=["tag1", "tag2"],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )
    
    advertDto = AdvertMapper.model_to_dto(advert)

    assert isinstance(advertDto, AdvertDto)    
    assert advertDto.title == advert.title
    assert advertDto.description == advert.description
    assert advertDto.price == advert.price
    assert advertDto.slug == advert.slug
    assert advertDto.owner == advert.owner
    assert advertDto.thumbnail == advert.thumbnail
    assert advertDto.tags == advert.tags