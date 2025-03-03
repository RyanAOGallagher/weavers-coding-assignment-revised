from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)

    changes = relationship("PromptChange", back_populates="prompt", cascade="all, delete-orphan")

class PromptChange(Base):
    __tablename__ = "prompt_changes"
    
    id = Column(Integer, primary_key=True, index=True)
    prompt_id = Column(Integer, ForeignKey("prompts.id", ondelete="CASCADE"))
    text = Column(Text, nullable=False)
    change_message = Column(String, nullable=False)
    
    prompt = relationship("Prompt", back_populates="changes")