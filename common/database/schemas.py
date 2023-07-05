from pydantic import BaseModel
from datetime import date


class Flow(BaseModel):
    id: str
    created: date
    updated: date
    projectId: str
    folderId: str

class Project(BaseModel):
    id: str
    created: date
    updated: date
    ownerId: str
    displayName: str
    notifyStatus: str

class User(BaseModel):
    id: str
    created: date
    updated: date
    email: str
    firstName: str
    lastName: str
    password: str
    status: str
    trackEvents: bool
    newsLetter: bool