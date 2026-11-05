from fastapi import APIRouter, Depends, HTTPException
from database.db import get_db
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.models import User, UserCreate, UserResponse
from utils.security import set_pwd_hash, verify_password

router = APIRouter()

@router.post("/register", response_model=UserResponse)

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Instanciar el objeto de SQLAlchemy sin el ID
    new_user = User(
        username=user.username,
        hashed_password=set_pwd_hash(user.password)
    )
    
    # Agregar y guardar en Supabase
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)  # Carga el ID autogenerado
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail=f"El usuario '{user.username}' ya existe."
        )
        
    # Retornar la instancia (FastAPI la filtra con UserResponse)
    return new_user

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist!")
    db.delete(user)
    db.commit()
    return {"message": "user deleted"}

@router.post("/login")
def login(user_data: UserCreate, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if not user:
        return HTTPException(status_code=404, detail="User not found!")
    is_valid = verify_password(user_data.password,user.hashed_password)
    if (is_valid):
        return {"message": "Succesly!"}
    else:
        return {"message": "incorrect!"}
