from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, DateTime, JSON
from database.db import Base
import datetime

class User(Base):
    __tablename__ = "users_table"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    isBan = Column(Boolean, default=False)

class Level(Base):
    __tablename__ = "levels_table"

    id = Column(String(11), primary_key=True, index=True)
    id_author = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    game_style = Column(Integer)
    theme = Column(String)
    time_of_day = Column(Integer)
    time_limit = Column(Integer)
    upload_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    level_data = Column(JSON)

class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    isBan: bool

    class Config:
        from_attributes = True

class LevelCreate(BaseModel):
    id: str
    id_author: int
    level_base64: str

class LevelResponse(BaseModel):
    id: str
    id_author: int
    title: str
    description: str
    game_style: int
    theme: str
    time_of_day: int
    time_limit: int
    upload_date: datetime.datetime
    
    class Config:
        from_attributes = True