from unittest.mock import Mock

from fastapi import HTTPException
import pytest
from app.advert.adverts_pq_repository import AdvertsPqRepository
from app.advert.adverts_service import AdvertsService
from app.advert.dto.create_advert_dto import CreateAdvertDto
from app.advert.dto.update_advert_dto import UpdateAdvertDto
from app.advert.entities.advert_entity import AdvertEntity


def test_read_advert_not_found():
    mock = Mock(spec=AdvertsPqRepository)
    mock.find_by_slug.return_value = None
    
    service = AdvertsService(repo=mock)

    with pytest.raises(HTTPException):
        service.read_advert("slug")
        
def test_read_advert():
    mock = Mock(spec=AdvertsPqRepository)
    mock.find_by_slug.return_value = {
        "slug": "slug",
        "thumbnail": "thumbnail",
        "title": "title",
        "description": "description",
        "price": 150.0,
        "owner": "owner",
        "tags": ["tags"]
    };
    
    service = AdvertsService(repo=mock)
    
    result = service.read_advert("slug")
    
    assert result == {
        "slug": "slug",
        "thumbnail": "thumbnail",
        "title": "title",
        "description": "description",
        "price": 150.0,
        "owner": "owner",
        "tags": ["tags"]
    }

def test_read_all():
    mock = Mock(spec=AdvertsPqRepository)
    mock.read_adverts.return_value = [
        {
            "slug": "slug",
            "thumbnail": "thumbnail",
            "title": "title",
            "description": "description",
            "price": 150.0,
            "owner": "owner",
            "tags": ["tags"]
        }
    ];
    
    service = AdvertsService(repo=mock)
    
    result = service.read_all_adverts()
    
    assert result == [
        {
            "slug": "slug",
            "thumbnail": "thumbnail",
            "title": "title",
            "description": "description",
            "price": 150.0,
            "owner": "owner",
            "tags": ["tags"]
        }
    ]

def test_create_advert():
    mock = Mock(spec=AdvertsPqRepository)
    mock.create_advert.return_value = {
        "id": 1,
        "slug": "title",
        "thumbnail": "thumbnail",
        "title": "title",
        "description": "description",
        "price": 150.0,
        "owner": "owner",
        "tags": ["tags"]
    };

    dto = CreateAdvertDto(
        thumbnail="thumbnail",
        title="title",
        description="description",
        price=150.0,
        owner="owner",
        tags=["tags"]
    )
    
    service = AdvertsService(repo=mock)
    result = service.create_advert(dto)
    
    assert result == {
        "id": 1,
        "slug": "title",
        "thumbnail": "thumbnail",
        "title": "title",
        "description": "description",
        "price": 150.0,
        "owner": "owner",
        "tags": ["tags"]
    }

def test_create_advert_unqiue():
    mock = Mock(spec=AdvertsPqRepository)
    mock.create_advert.side_effect = Exception("Advert title must be unique")
    
    dto = CreateAdvertDto(
        thumbnail="thumbnail",
        title="title",
        description="description",
        price=150.0,
        owner="owner",
        tags=["tags"]
    )
    
    service = AdvertsService(repo=mock)
    
    with pytest.raises(HTTPException):
        service.create_advert(dto)

def test_update_advert_not_found():
    mock = Mock(spec=AdvertsPqRepository)
    mock.find_by_slug.return_value = None
    
    service = AdvertsService(repo=mock)
    
    with pytest.raises(HTTPException):
        service.update_advert("slug", "dto")
        
def test_update_advert():
    mock = Mock(spec=AdvertsPqRepository)
    mock.find_by_slug.return_value = AdvertEntity(
        id=1,
        slug="title",
        thumbnail="thumbnail",
        title="title",
        description="description",
        price=150.0,
        owner="owner",
        tags=["tags"]
    );
    
    mock.update_advert.return_value = {
        "id":1,
        "slug":"title",
        "thumbnail":"thumbnail",
        "title":"title",
        "description":"description",
        "price":350.0,
        "owner":"owner",
        "tags":["tags"]
    }
    
    dto = UpdateAdvertDto(
        price=350.0,
    )
    
    service = AdvertsService(repo=mock)
    result = service.update_advert("slug", dto)
    
    assert result == {
        "id": 1,
        "slug": "title",
        "thumbnail": "thumbnail",
        "title": "title",
        "description": "description",
        "price": 350.0,
        "owner": "owner",
        "tags": ["tags"]
    }

def test_update_advert_unique():
    mock = Mock(spec=AdvertsPqRepository)
    mock.find_by_slug.return_value = AdvertEntity(
        id=1,
        slug="title",
        thumbnail="thumbnail",
        title="title",
        description="description",
        price=150.0,
        owner="owner",
        tags=["tags"]
    );
    
    mock.update_advert.side_effect = Exception("Advert title must be unique")
    
    dto = UpdateAdvertDto(
        price=350.0,
    )
    
    service = AdvertsService(repo=mock)
    
    with pytest.raises(HTTPException):
        service.update_advert("slug", dto)
    