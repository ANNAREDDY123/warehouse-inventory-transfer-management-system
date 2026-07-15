from pydantic import (
    BaseModel,
    Field
)


class ProductCreate(BaseModel):

    product_name: str = Field(..., min_length=3)

    sku: str = Field(..., min_length=3)

    stock_quantity: int = Field(..., gt=0)

    unit_price: float = Field(..., gt=0)
