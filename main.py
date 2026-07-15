import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.auth import router as auth_router
from routes.warehouses import router as warehouses_router
from routes.products import router as products_router
from routes.transfers import router as transfers_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Warehouse Inventory Transfer Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(warehouses_router)
app.include_router(products_router)
app.include_router(transfers_router)


@app.get("/")
def home():

    logger.info("Application Started Successfully")

    return {
        "message": "Warehouse Inventory Transfer Management System"
    }
