from ast import List
from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar('T')

class IdeationResponse(BaseModel):
    response = []

class ResearchResponse(BaseModel):
    response: str