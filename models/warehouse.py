from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from database import Base


class Warehouse(Base):

    __tablename__ = "warehouses"

    id = Column(
        Integer,
        primary_key=True
    )

    warehouse_name = Column(String)

    location = Column(String)

    manager_name = Column(String)

    is_active = Column(Boolean)
