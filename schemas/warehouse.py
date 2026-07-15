from pydantic import (
    BaseModel,
    Field
)


class WarehouseCreate(BaseModel):

    warehouse_name: str = Field(..., min_length=3)

    location: str = Field(..., min_length=3)

    manager_name: str = Field(..., min_length=3)

    is_active: bool
