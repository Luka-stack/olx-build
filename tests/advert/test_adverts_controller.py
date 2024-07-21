import datetime
from http import HTTPStatus
from unittest import mock
from fastapi import HTTPException
import pytest
from unittest.mock import Mock, patch
from fastapi.testclient import TestClient

from app.advert.adverts_service import AdvertsService
from app.advert.dto.advert_dto import AdvertDto
from app.server import app

mock_advert_service = Mock(spec=AdvertsService)
app.dependency_overrides[AdvertsService] = lambda: mock_advert_service

client = TestClient(app)

def test_read_advert():
    mock_advert_service.read_advert.return_value = AdvertDto(
        slug="str",
        thumbnail="str",
        title="str",
        description="str",
        price=150.0,
        owner="str",
        created_at="2021-01-01T00:00:00",
        updated_at="2021-01-01T00:00:00",
        tags=["str"]
    )
    
    response = client.get("/adverts/1")
    
    assert response.status_code == 200
    assert response.json() == {
        "slug":"str",
        "thumbnail":"str",
        "title":"str",
        "description":"str",
        "price":150.0,
        "owner":"str",
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
        "tags": ["str"]
    }
    
def test_read_advert_not_found():
    mock_advert_service.read_advert.side_effect = HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Advert not found")
    
    response = client.get("/adverts/1")
    
    assert response.status_code == 404
    assert response.json() == {"detail": "Advert not found"}
    
def test_read_all():
    mock_advert_service.read_all_adverts.return_value = [
        AdvertDto(
            slug="str",
            thumbnail="str",
            title="str",
            description="str",
            price=150.0,
            owner="str",
            created_at="2021-01-01T00:00:00",
            updated_at="2021-01-01T00:00:00",
            tags=["str"]
        )
    ]
    
    response = client.get("/adverts/")
    
    assert response.status_code == 200
    assert response.json() == [
        {
            "slug":"str",
            "thumbnail":"str",
            "title":"str",
            "description":"str",
            "price":150.0,
            "owner":"str",
            "created_at": "2021-01-01T00:00:00",
            "updated_at": "2021-01-01T00:00:00",
            "tags": ["str"]
        }
    ]
    
def test_create_advert():
    mock_advert_service.create_advert.return_value = AdvertDto(
        slug="str",
        thumbnail="str",
        title="str",
        description="str",
        price=150.0,
        owner="str",
        created_at="2021-01-01T00:00:00",
        updated_at="2021-01-01T00:00:00",
        tags=["str"]
    )
    
    response = client.post("/adverts/", json={
        "thumbnail": "str",
        "title": "str",
        "description": "str",
        "price": 150.0,
        "owner": "str",
        "tags": ["str"]
    })
    
    assert response.status_code == 201
    assert response.json() == {
        "slug":"str",
        "thumbnail":"str",
        "title":"str",
        "description":"str",
        "price":150.0,
        "owner":"str",
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
        "tags": ["str"]
    }
    
def test_update_advert():
    mock_advert_service.update_advert.return_value = AdvertDto(
        slug="str",
        thumbnail="str",
        title="str",
        description="str",
        price=150.0,
        owner="str",
        created_at="2021-01-01T00:00:00",
        updated_at="2021-01-01T00:00:00",
        tags=["str"]
    )
    
    response = client.patch("/adverts/1", json={
        "thumbnail": "str",
        "title": "str",
        "description": "str",
        "price": 150.0,
        "owner": "str",
        "tags": ["str"]
    })
    
    assert response.status_code == 200
    assert response.json() == {
        "slug":"str",
        "thumbnail":"str",
        "title":"str",
        "description":"str",
        "price":150.0,
        "owner":"str",
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
        "tags": ["str"]
    }
    
def test_delete_advert():
    response = client.delete("/adverts/1")
    
    assert response.status_code == 204
    assert response.text == ""