from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#conexão com o db
DATABASE_URL = 'mysql://root:@localhost/fastapi_db'

engine = create_engine(DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependência para obter a sessão do banco
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()