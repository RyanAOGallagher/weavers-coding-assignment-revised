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

# Ability to view, add, edit, and delete prompts. 
# Ability to leave a change message when editing a prompt. 
# Ability to view the history of changes for each prompt.

@app.get("/")
def read_root():
    return {"message": "App root."}

#Get all prompts
@app.get("/prompts/", response_model=List[PromptResponse])
def get_prompts(db: db_dependency):
    prompts = db.query(models.Prompt).all()
    return prompts

#Get a single prompt by ID
@app.get("/prompts/{prompt_id}/", response_model=PromptResponse)
def get_prompt(prompt_id: int, db: db_dependency): 
    result = db.query(models.Prompt).filter(models.Prompt.id == prompt_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return result

#Create a new prompt
@app.post("/prompts/", response_model=dict)
def create_prompt(prompt: PromptCreate, db: db_dependency):
    db_prompt = models.Prompt(text=prompt.text)
    db.add(db_prompt)
    db.commit()
    db.refresh(db_prompt)
    return {"message": "Prompt created successfully"}

#Update a prompt
@app.put("/prompts/{prompt_id}/", response_model=dict)
def update_prompt(prompt_id: int, prompt: PromptUpdate, db: db_dependency):
    db_prompt = db.query(models.Prompt).filter(models.Prompt.id == prompt_id).first()

    if not db_prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")

    change_record = models.PromptChange(prompt_id=prompt_id, text=prompt.text, change_message=prompt.change_message)
    db.add(change_record)

    db_prompt.text = prompt.text

    db.commit()
    db.refresh(db_prompt)
    return {"message": "Prompt updated successfully"}


#Delete a prompt
@app.delete("/prompts/{prompt_id}/", response_model=dict)
def delete_prompt(prompt_id: int, db: db_dependency):
    db_prompt = db.query(models.Prompt).filter(models.Prompt.id == prompt_id).first()
    if not db_prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")

    db.delete(db_prompt) 
    db.commit()

    return {"message": "Prompt deleted successfully"}


#Get the history of changes for a prompt
@app.get("/prompts/{prompt_id}/history", response_model=List[ChangeResponse])
def get_prompt_history(prompt_id: int, db: db_dependency):
    prompt = db.query(models.Prompt).filter(models.Prompt.id == prompt_id).first()
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    changes = db.query(models.PromptChange).filter(models.PromptChange.prompt_id == prompt_id).all()
    
    return changes
