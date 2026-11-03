from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.schemas.product import ProductCreate
from app.models.product_model import Product
from app.database.database import SessionLocal

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    new_product = Product(
        key=product.key,
        name=product.name,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "success": True,
        "data": {
            "id": new_product.id
        }
    }


@router.get("/products/{key}")
def get_product(
    key: str,
    db: Session = Depends(get_db)
):

    product = (
        db.query(Product)
        .filter(Product.key == key)
        .first()
    )

    if not product:

        return {
            "success": False,
            "message": "Producto no encontrado"
        }

    return {
        "success": True,
        "data": {
            "key": product.key,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }
    }