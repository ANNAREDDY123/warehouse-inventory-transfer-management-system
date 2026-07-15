from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True
    )

    product_name = Column(String)

    sku = Column(
        String,
        unique=True
    )

    stock_quantity = Column(Integer)

    unit_price = Column(Float)
