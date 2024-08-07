from fastapi import FastAPI

from app.logger import LoggingMiddleware
from app.database import Base, engine
from app.advert.adverts_controller import router as advert_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registering the routers
app.include_router(advert_router)

# Registering the middlewares
app.add_middleware(LoggingMiddleware)
