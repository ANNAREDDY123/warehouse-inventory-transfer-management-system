from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models.warehouse import Warehouse
from schemas.warehouse import WarehouseCreate

router = APIRouter(
    prefix="/warehouses",
    tags=["Warehouses"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_warehouse(
    warehouse: WarehouseCreate,
    db: Session = Depends(get_db)
):

    db_warehouse = Warehouse(**warehouse.dict())

    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)

    return db_warehouse


@router.get("/")
def get_warehouses(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Warehouse)

    total = query.count()

    warehouses = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "total_records": total,
        "current_page": page,
        "limit": limit,
        "data": warehouses
    }


@router.get("/{warehouse_id}")
def get_warehouse(
    warehouse_id: int,
    db: Session = Depends(get_db)
):

    warehouse = db.query(Warehouse).filter(
        Warehouse.id == warehouse_id
    ).first()

    if not warehouse:
        raise HTTPException(
            status_code=404,
            detail="Warehouse not found."
        )

    return warehouse


@router.put("/{warehouse_id}")
def update_warehouse(
    warehouse_id: int,
    warehouse: WarehouseCreate,
    db: Session = Depends(get_db)
):

    db_warehouse = db.query(Warehouse).filter(
        Warehouse.id == warehouse_id
    ).first()

    if not db_warehouse:
        raise HTTPException(
            status_code=404,
            detail="Warehouse not found."
        )

    db_warehouse.warehouse_name = warehouse.warehouse_name
    db_warehouse.location = warehouse.location
    db_warehouse.manager_name = warehouse.manager_name
    db_warehouse.is_active = warehouse.is_active

    db.commit()

    return {
        "message": "Warehouse updated successfully."
    }


@router.delete("/{warehouse_id}")
def delete_warehouse(
    warehouse_id: int,
    db: Session = Depends(get_db)
):

    warehouse = db.query(Warehouse).filter(
        Warehouse.id == warehouse_id
    ).first()

    if not warehouse:
        raise HTTPException(
            status_code=404,
            detail="Warehouse not found."
        )

    db.delete(warehouse)
    db.commit()

    return {
        "message": "Warehouse deleted successfully."
    }
