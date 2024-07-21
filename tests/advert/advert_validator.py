from app.advert.advert_validator import AdvertValidator


def test_validate_create_advert():
    correct = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "price": 100.0,
        "owner": "owner",
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_create_advert(correct)
    
    assert result == True
    
def test_validate_create_advert_missing_thumbnail():
    missing_thumbnail = {
        "title": "Title",
        "description": "Description",
        "price": 100.0,
        "owner": "owner",
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_create_advert(missing_thumbnail)
    
    assert result == False
    
def test_validate_create_advert_missing_title():
    missing_title = {
        "thumbnail": "thumbnail",
        "description": "Description",
        "price": 100.0,
        "owner": "owner",
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_create_advert(missing_title)
    
    assert result == False
    
def test_validate_create_advert_missing_description():
    missing_description = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "price": 100.0,
        "owner": "owner",
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_create_advert(missing_description)
    
    assert result == False
    
def test_validate_create_advert_missing_price():
    missing_price = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "owner": "owner",
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_create_advert(missing_price)
    
    assert result == False

def test_validate_create_advert_price_not_float():
    price_not_float = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "owner": "owner",
        "price": "100.0",
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_create_advert(price_not_float)
    
    assert result == False

def test_validate_create_advert_negative_price():
    negative_price = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "price": -100.0,
        "owner": "owner",
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_create_advert(negative_price)
    
    assert result == False
    
def test_validate_create_tags_type():
    correct = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "price": -100.0,
        "owner": "owner",
        "tags": "tag1",
    }
    
    result = AdvertValidator.validate_create_advert(correct)
        
    assert result == False
    
def test_validate_create_advert_missing_owner():
    missing_owner = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "price": 100.0,
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_create_advert(missing_owner)
    
    assert result == False

def test_validate_create_advert_missing_tags():
    missing_tags = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "price": 100.0,
        "owner": "owner",
    }
    
    result = AdvertValidator.validate_create_advert(missing_tags)
    
    assert result == False
    
def test_validate_update_advert():
    correct = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "price": 100.0,
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_update_advert(correct)
    
    assert result == True
    
def test_validate_update_advert_missing_thumbnail():
    missing_thumbnail = {
        "title": "Title",
        "description": "Description",
        "price": 100.0,
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_update_advert(missing_thumbnail)
    
    assert result == True
    
def test_validate_update_advert_missing_title():
    missing_title = {
        "thumbnail": "thumbnail",
        "description": "Description",
        "price": 100.0,
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_update_advert(missing_title)
    
    assert result == True
    
def test_validate_update_advert_missing_description():
    missing_description = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "price": 100.0,
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_update_advert(missing_description)
    
    assert result == True
    
def test_validate_update_advert_missing_price():
    missing_price = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_update_advert(missing_price)
    
    assert result == True
    
def test_validate_update_advert_price_not_float():
    price_not_float = {
        "price": "100.0",
    }
    
    result = AdvertValidator.validate_update_advert(price_not_float)
    
    assert result == False
    
def test_validate_update_advert_negative_price():
    negative_price = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "price": -100.0,
        "tags": ["tag1", "tag2"],
    }
    
    result = AdvertValidator.validate_update_advert(negative_price)
    
    assert result == False
    
def test_validate_update_advert_missing_tags():
    missing_tags = {
        "thumbnail": "thumbnail",
        "title": "Title",
        "description": "Description",
        "price": 100.0,
    }
    
    result = AdvertValidator.validate_update_advert(missing_tags)
    
    assert result == True

def test_validate_update_tags_type():
    correct = {
        "tags": "tag1",
    }
    
    result = AdvertValidator.validate_update_advert(correct)
        
    assert result == False