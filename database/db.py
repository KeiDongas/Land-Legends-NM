import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.environ.get('DB_URL')

engine = create_engine(DATABASE_URL, pool_pre_ping=True) #pool_pre_ping verifica si la conexion sigue activa antes de mandar cualquier solicitud

#Constructor de sesiones (objetos tipo sesion)
SessionLocal = sessionmaker(bind=engine)

#Base para todos los modelos de tablas
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


