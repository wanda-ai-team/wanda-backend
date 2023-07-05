from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from .database import Base


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