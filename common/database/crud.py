from sqlalchemy.orm import Session

from . import models, schemas

def get_flow_by_flowId(db: Session, flowId: str):
    return db.query(models.Flow).filter(models.Flow.id == flowId).first()

def get_project_by_projectId(db: Session, projectId: str):
    return db.query(models.Project).filter(models.Project.id == projectId).first()

def get_user_by_userId(db: Session, userId: str):
    return db.query(models.User).filter(models.User.id == userId).first()