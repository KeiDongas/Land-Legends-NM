from fastapi import FastAPI, Depends, HTTPException
from database.db import engine, Base, get_db
from routers import users, levels

 
Base.metadata.create_all(bind=engine) #creacion de tablas tan pronto inicia el programa

app = FastAPI()

@app.get("/")
def root():
    return {"message": "working","author": "elabusador"}

app.include_router(users.router)
app.include_router(levels.router)