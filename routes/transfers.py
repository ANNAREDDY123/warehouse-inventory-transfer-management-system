from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.transfer import Transfer
from models.product import Product
from models.warehouse import Warehouse

from schemas.transfer import TransferCreate

from services.transfer_service import (
    valid_transfer_status,
    same_warehouse,
    sufficient_stock
)

router = APIRouter(
    prefix="/transfers",
    tags=["Transfers"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_transfer(
    transfer: TransferCreate,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == transfer.product_id
    ).first()

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product not found."
        )

    source = db.query(Warehouse).filter(
        Warehouse.id == transfer.from_warehouse
    ).first()

    destination = db.query(Warehouse).filter(
        Warehouse.id == transfer.to_warehouse
    ).first()

    if not source or not destination:

        raise HTTPException(
            status_code=404,
            detail="Warehouse not found."
        )

    if same_warehouse(
        transfer.from_warehouse,
        transfer.to_warehouse
    ):

        raise HTTPException(
            status_code=400,
            detail="Source and destination warehouses cannot be the same."
        )

    if not sufficient_stock(
        product.stock_quantity,
        transfer.quantity
    ):

        raise HTTPException(
            status_code=400,
            detail="Insufficient stock available."
        )

    if not valid_transfer_status(
        transfer.status
    ):

        raise HTTPException(
            status_code=400,
            detail="Invalid transfer status."
        )

    db_transfer = Transfer(
        from_warehouse=transfer.from_warehouse,
        to_warehouse=transfer.to_warehouse,
        product_id=transfer.product_id,
        quantity=transfer.quantity,
        transfer_date=transfer.transfer_date,
        status=transfer.status
    )

    if transfer.status == "Completed":

        product.stock_quantity -= transfer.quantity

    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)

    return db_transfer


@router.get("/")
def get_transfers(
    status: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Transfer)

    if status:

        query = query.filter(
            Transfer.status == status
        )

    total = query.count()

    transfers = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": transfers
    }


@router.get("/{transfer_id}")
def get_transfer(
    transfer_id: int,
    db: Session = Depends(get_db)
):

    transfer = db.query(Transfer).filter(
        Transfer.id == transfer_id
    ).first()

    if not transfer:

        raise HTTPException(
            status_code=404,
            detail="Transfer not found."
        )

    return transfer


@router.put("/{transfer_id}")
def update_transfer(
    transfer_id: int,
    transfer: TransferCreate,
    db: Session = Depends(get_db)
):

    db_transfer = db.query(Transfer).filter(
        Transfer.id == transfer_id
    ).first()

    if not db_transfer:

        raise HTTPException(
            status_code=404,
            detail="Transfer not found."
        )

    if db_transfer.status == "Cancelled":

        raise HTTPException(
            status_code=400,
            detail="Cancelled transfers cannot be updated."
        )

    db_transfer.status = transfer.status

    db.commit()

    return {
        "message": "Transfer updated successfully."
    }


@router.get("/reports/inventory")
def warehouse_inventory(
    db: Session = Depends(get_db)
):

    return db.query(Product).all()
