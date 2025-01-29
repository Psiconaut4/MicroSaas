from fastapi import FastAPI
from data.database import Base, engine
from routes.products import router as products_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode ser configurado para aceitar apenas o domínio do Vue
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products_router)

Base.metadata.create_all(bind=engine)

