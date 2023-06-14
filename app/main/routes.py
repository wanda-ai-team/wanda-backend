from fastapi import APIRouter

mainRouter = APIRouter()

@mainRouter.get('/')
def index():
    return 'This is The Main Blueprint'