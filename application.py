from flask import Flask
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
import random   # needed for generating a random number for an API
import uvicorn  # optional if you run it directly from terminal

application = app = FastAPI()
application.debug = True


# Initialize Flask extensions here

# Register blueprints here
# from app.agents import bp as agents_bp
# application.register_blueprint(agents_bp, url_prefix='/agents')

# from app.main import bp as main_bp
# application.register_blueprint(main_bp)

@app.get("/test", response_class=PlainTextResponse)
async def hello():
    return "Hello World!"

from app.agents import *

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    uvicorn.run("application:application")
