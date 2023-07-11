from pydantic import BaseModel
from datetime import date


class Flow(BaseModel):
    id: str
    created: date
    updated: date
    projectId: str
    folderId: str

class FlowRun(BaseModel):
    id: str
    created: date
    updated: date
    projectId: str
    flowId: str
    flowVersionId: str
    environment: str
    flowDisplayName: str
    logsFileId: str
    status: str
    startTime: date
    finishTime: date
    pauseMetadata: str

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

class ResearchTopics(BaseModel):
    id: str
    topic: str