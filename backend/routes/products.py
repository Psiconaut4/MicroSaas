from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from data.database import get_db
from data.models import Product

router = APIRouter(prefix='/products', tags=['Products'])

# Modelo Pydantic para validação
class ProductCreate(BaseModel):
    name: str
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Permite conversão de ORM para Pydantic

@router.post("/", response_model=ProductCreate, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(name=product.name, price=product.price)
    db.add(new_product)
    try:
        db.commit()
        db.refresh(new_product)
        return new_product
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao salvar produto")
    finally:
        db.close()


@router.get("/", response_model=list[ProductResponse])
def get_product(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.delete("/", status_code=200)
def del_product(name: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.name == name).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Produto deletado com sucesso"}

