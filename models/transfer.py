from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from database import Base


class Transfer(Base):

    __tablename__ = "transfers"

    id = Column(
        Integer,
        primary_key=True
    )

    from_warehouse = Column(
        Integer,
        ForeignKey("warehouses.id")
    )

    to_warehouse = Column(
        Integer,
        ForeignKey("warehouses.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column(Integer)

    transfer_date = Column(Date)

    status = Column(String)
