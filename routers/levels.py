import base64
import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Level, LevelCreate, LevelResponse

router = APIRouter()

@router.post("/create")
def create_level(level_data: LevelCreate, db: Session = Depends(get_db)):
    try:
        decoded_bytes = base64.b64decode(level_data.level_base64)
        level_json = json.loads(decoded_bytes.decode('utf-8'))
    except Exception:
        raise HTTPException(status_code=400, detail="The Base64 file is invalid")

    try:
        meta_data = level_json["ROOT"][0]["AJUSTES"][0]
        
        title = meta_data.get("title", "Untitled level")
        description = meta_data.get("desc", "No description")
        game_style = meta_data.get("game_style", 1)
        theme = meta_data.get("gametheme", "ground") 
        time_limit = meta_data.get("timer", 300)
        time_of_day = 0 
        
    except (KeyError, IndexError):
        raise HTTPException(status_code=400, detail="The file does not have the expected format")

    existing_level = db.query(Level).filter(Level.id == level_data.id).first()
    if existing_level:
        raise HTTPException(status_code=400, detail="The ID for this level already exists")

    new_level = Level(
        id=level_data.id,
        id_author=level_data.id_author,
        title=title,
        description=description,
        game_style=game_style,
        theme=theme,
        time_of_day=time_of_day,
        time_limit=time_limit,
        level_data=level_data.level_base64 
    )
    
    db.add(new_level)
    db.commit()
    db.refresh(new_level)
    
    return {"message": "Level uploaded successfully", "level_id": new_level.id}


@router.get("/", response_model=list[LevelResponse])
def get_all_levels(db: Session = Depends(get_db)):
    levels = db.query(Level).all()
    return levels


@router.get("/{level_id}")
def get_level(level_id: str, db: Session = Depends(get_db)):
    level = db.query(Level).filter(Level.id == level_id).first()
    
    if not level:
        raise HTTPException(status_code=404, detail="Level not found")
    
    return {
        "id": level.id,
        "id_author": level.id_author,
        "title": level.title,
        "description": level.description,
        "game_style": level.game_style,
        "theme": level.theme,
        "time_of_day": level.time_of_day,
        "time_limit": level.time_limit,
        "level_base64": level.level_data
    }