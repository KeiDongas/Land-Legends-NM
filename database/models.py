from pydantic import BaseModel, Field
from sqlalchemy import Boolean, Column, Integer, String, BigInteger
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
    __tablename__ = "users_table"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    isBan = Column(Boolean, default=False)

class LevelModel(BaseModel):
    id: str
    id_author:int
    title:str
    description:str
    game_style:str
    theme:str
    time_of_day:int
    time_limit:int
    upload_date:str

class Level(Base):
    __tablename__ = "levels_table"

    id=Column(String(11), primary_key=True, index=True)
    id_author=Column(Integer)
    title=Column(String)
    description=Column(String)
    game_style=Column(String)
    theme = Column(String)
    time_of_day = Column(Integer)
    time_limit = Column(Integer)
    upload_date = Column(String)
    