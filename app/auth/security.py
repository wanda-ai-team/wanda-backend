
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Depends, HTTPException, Request, status
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
    if api_key in api_keys:
        return "pass"

    db_flow_run = crud.get_flowId_by_flowVersionId(db, flowVersionId=api_key)
    print("db_flow_run")
    print(db_flow_run)
    print(api_key)
    return "pass"
    if(db_flow_run is None):
        raise_exception()
    elif(db_flow_run.flowId is None):
        raise_exception()
    else:
        db_flow = crud.get_flow_by_flowId(db, flowId=db_flow_run.flowId)
        print("db_flow")
        print(db_flow)

        if(db_flow is None):
            raise_exception()
        elif(db_flow.projectId is None):
            raise_exception()
        else:
            db_project = crud.get_project_by_projectId(db, projectId=db_flow.projectId)
            print("db_project")
            print(db_project)
        
            if(db_project is None):
                raise_exception()
            elif(db_project.ownerId is None):
                raise_exception()
            # else:
            #     db_user = crud.get_user_by_userId(db, userId=db_project.ownerId)
            #     print("db_user")
            #     print(db_user)
            #     if(db_user is None):
            #         raise_exception()
            #     else:
            #         if(db_user.status == "VERIFIED"):
            #             return "pass"
            #         else:
            #             raise_exception()
    

    