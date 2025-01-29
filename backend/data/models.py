from sqlalchemy import Column, Integer, String, Float
from data.database import Base
from pydantic import BaseModel

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float(4), unique=True, nullable=False)

class ProductCreate(BaseModel):
    name: str
    price: float