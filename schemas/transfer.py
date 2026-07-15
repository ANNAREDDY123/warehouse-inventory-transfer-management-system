from pydantic import (
    BaseModel,
    Field
)

from datetime import date


class TransferCreate(BaseModel):

    from_warehouse: int

    to_warehouse: int

    product_id: int

    quantity: int = Field(..., gt=0)

    transfer_date: date

    status: str
