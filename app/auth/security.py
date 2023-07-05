
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import os
from common.database import crud

from common.database.database import SessionLocal

load_dotenv()

api_keys = [os.getenv("API_KEY")]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def raise_exception():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden"
    )

def get_api_key(api_key: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    db_flow = crud.get_flow_by_flowId(db, flowId=api_key)
    if(db_flow is None):
        raise_exception()
    elif(db_flow.projectId is None):
        raise_exception()
    else:
        db_project = crud.get_project_by_projectId(db, projectId=db_flow.projectId)
    
        if(db_project is None):
            raise_exception()
        elif(db_project.ownerId is None):
            raise_exception()
        else:
            db_user = crud.get_user_by_userId(db, userId=db_project.ownerId)
                
            if(db_user is None):
                raise_exception()
            else:
                if(db_user.status == "VERIFIED"):
                    return "pass"
                else:
                    raise_exception()
    

    