from pydantic import BaseModel

class PromptCreate(BaseModel):
    text: str

    class Config:
        from_attributes = True


class PromptUpdate(BaseModel):
    text: str
    change_message: str

    class Config:
        from_attributes = True


class PromptResponse(BaseModel):  # Response model for prompts
    id: int
    text: str

    class Config:
        from_attributes = True


class ChangeResponse(BaseModel):  
    id: int  # ID is always present when retrieving changes
    prompt_id: int  
    text: str
    change_message: str  

