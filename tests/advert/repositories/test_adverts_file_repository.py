import pytest
import datetime

from app.advert.models.advert import Advert
from app.advert.repositories.adverts_file_repository import AdvertsFileRepository

def test_create_advert():
    expected = Advert(
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
    
    repo = AdvertsFileRepository()
    
    len_before = len(repo.read_adverts())
    result = repo.create_advert(expected)
    len_after = len(repo.read_adverts())

    assert len_before + 1 == len_after
    
    assert isinstance(result.id, int)
    assert result.title == expected.title
    assert result.description == expected.description
    assert result.price == expected.price
    assert result.slug == expected.slug
    assert result.owner == expected.owner
    assert result.thumbnail == expected.thumbnail
    assert result.tags == expected.tags
    assert isinstance(result.created_at, datetime.datetime)
    assert isinstance(result.updated_at, datetime.datetime)

def test_create_advert_slug_config():
    model = Advert(
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
    
    repo = AdvertsFileRepository()
    
    repo.create_advert(model)
    
    with pytest.raises(Exception):
        repo.create_advert(model)

def test_read_adverts():
    expected = [Advert(
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
    )]
    
    repo = AdvertsFileRepository()
    
    results = repo.read_adverts()
    
    assert len(results) == len(expected)
    assert results[0].id == expected[0].id
    
def delete_adverts():
    expected = [Advert(
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
    )]
    
    repo = AdvertsFileRepository()
    
    before_len = len(repo.read_adverts())
    repo.delete_advert(expected[0].slug)
    after_len = len(repo.read_adverts())
    
    assert before_len == after_len + 1
    
def test_find_by_slug():
    expected = Advert(
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
    
    repo = AdvertsFileRepository()
    
    repo.create_advert(expected)
    
    result = repo.find_by_slug(expected.slug)
    
    assert result.id == expected.id
    assert result.title == expected.title
    assert result.description == expected.description
    assert result.price == expected.price
    assert result.slug == expected.slug
    assert result.owner == expected.owner
    assert result.thumbnail == expected.thumbnail
    assert result.tags == expected.tags
    assert isinstance(result.created_at, datetime.datetime)
    assert isinstance(result.updated_at, datetime.datetime)
    
def test_find_by_slug_not_found():
    repo = AdvertsFileRepository()
    
    result = repo.find_by_slug("slug")
    
    assert result is None
    
def test_update_advert():
    expected = Advert(
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
    
    repo = AdvertsFileRepository()
    
    repo.create_advert(expected)
    
    expected.description = "New Description"
    expected.price = 200.0
    expected.owner = "new owner"
    
    result = repo.update_advert(expected.slug, expected)
    
    assert result.id == expected.id
    assert result.title == expected.title
    assert result.description == expected.description
    assert result.price == expected.price
    assert result.slug == expected.slug
    assert result.owner == expected.owner
    assert result.updated_at != expected.updated_at
    assert result.thumbnail == expected.thumbnail
    assert result.tags == expected.tags
    assert isinstance(result.created_at, datetime.datetime)
    assert isinstance(result.updated_at, datetime.datetime)
    
def test_update_advert_slug_conflict():
    expected = Advert(
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
    
    repo = AdvertsFileRepository()
    repo.create_advert(expected)

    expected.price = 200.0
    
    with pytest.raises(Exception):
        repo.update_advert(expected.slug, expected)