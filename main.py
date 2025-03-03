from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from schemas import PromptCreate, PromptUpdate, PromptResponse, ChangeResponse

app = FastAPI()

models.Base.metadata.create_all(bind=engine) 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]