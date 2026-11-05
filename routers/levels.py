from fastapi import APIRouter, Depends, HTTPException
from database.models import LevelModel, Level
from database.db import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

router = APIRouter()

@router.get("/search/{level_id}", response_model=LevelModel)
def get_level_byId(level_id: str, db: Session = Depends(get_db)):
    level = db.query(Level).filter(Level.id == level_id).first()
    if not level:
        raise HTTPException(status_code=404, detail="Level not found!")
    return level

@router.post("/create", response_model=LevelModel)
def create_level(level: LevelModel, db: Session = Depends(get_db)):
  # Convierte el esquema de Pydantic directamente a los argumentos del modelo de SQLAlchemy
  new_level = Level(**level.model_dump())

  db.add(new_level)
  try:
    db.commit()
    db.refresh(new_level)
  except Exception as e:
    db.rollback()
    raise HTTPException(
        status_code=400, detail=f"Error al insertar el nivel: {str(e)}"
    )

  return new_level