import datetime
from sqlalchemy import Column, Integer, String, Float, JSON, DateTime

from app.database import Base


class AdvertEntity(Base):
    __tablename__ = 'adverts'
    
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True)
    thumbnail = Column(String)
    title = Column(String, unique=True)
    description = Column(String)
    price = Column(Float)
    owner = Column(String)
    tags = Column(JSON)
    
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    