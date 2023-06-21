
from dotenv import load_dotenv
from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os

load_dotenv()

api_keys = [os.getenv("API_KEY")]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # use token authentication


def get_api_key(api_key: str = Depends(oauth2_scheme)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden"
        )
