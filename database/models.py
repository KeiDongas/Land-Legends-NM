from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String
from database.db import Base

# esquema para recibir la entrada (POST /users)
class UserCreate(BaseModel):
    username: str
    password: str

# esquema para moldear la respuesta JSON al cliente
class UserResponse(BaseModel):
    id: int
    username: str
    isBan: bool

    class Config:
        from_attributes = True  # Permite mapear desde el objeto de SQLAlchemy

# modelo de la Base de Datos (SQLAlchemy)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    isBan = Column(Boolean, default=False)