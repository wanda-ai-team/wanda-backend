from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from .database import Base


class FlowRun(Base):
    __tablename__ = "flow_run"

    id = Column(String, primary_key=True, index=True)
    created = Column(Date)
    updated = Column(Date)
    projectId = Column(String)
    flowId = Column(String)
    flowVersionId = Column(String)
    environment = Column(String)
    flowDisplayName = Column(String)
    logsFileId = Column(String)
    status = Column(String)
    startTime = Column(Date)
    finishTime = Column(Date)
    pauseMetadata = Column(String)

class FlowVersion(Base):
    __tablename__ = "flow_version"

    id = Column(String, primary_key=True, index=True)
    created = Column(Date)
    updated = Column(Date)
    flowId = Column(String)
    displayName = Column(String)
    trigger = Column(String)
    valid = Column(Boolean)
    state = Column(String)
    
class Flow(Base):
    __tablename__ = "flow"

    id = Column(String, primary_key=True, index=True)
    created = Column(Date)
    updated = Column(Date)
    projectId = Column(String)
    folderId = Column(String)


class Project(Base):
    __tablename__ = "project"

    id = Column(String, primary_key=True, index=True)
    created = Column(Date)
    updated = Column(Date)
    ownerId = Column(String)
    displayName = Column(String)
    notifyStatus = Column(String)

class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True, index=True)
    created = Column(Date)
    updated = Column(Date)
    email = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    password = Column(String)
    status = Column(String)
    trackEvents = Column(Boolean)
    newsLetter = Column(Boolean)

class ResearchTopics(Base):
    __tablename__ = "research_topics"

    id = Column(String, primary_key=True, index=True, autoincrement=True)
    topic = Column(String)