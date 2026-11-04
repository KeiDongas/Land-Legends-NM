from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from database.db import engine, Base, get_db
from database.models import User, UserCreate, UserResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "working","author": "elabusador"}

@app.post("/register", response_model=UserResponse)

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Instanciar el objeto de SQLAlchemy sin el ID
    new_user = User(
        username=user.username,
        password=user.password
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

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist!")
    db.delete(user)
    db.commit()
    return {"message": "user deleted"}
