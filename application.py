from app.auth.security import get_api_key
from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
import uvicorn  # optional if you run it directly from terminal
from app.main.routes import mainRouter
from app.agents.routes import agentsRouter
from app.llmTools.routes import llmToolsRouter
from firebase_admin import  credentials
import firebase_admin
import os

application = app = FastAPI()

@app.get("/test", response_class=PlainTextResponse)
async def hello():
    return "Hello World!"


application.include_router(agentsRouter, prefix="/agents", dependencies=[Depends(get_api_key)])
application.include_router(llmToolsRouter, prefix="/llmTools", dependencies=[Depends(get_api_key)])
application.include_router(mainRouter, prefix="/main", dependencies=[Depends(get_api_key)])
# Setting debug to True enables debug output. This line should be
# removed before deploying a production app.

cred = credentials.Certificate({
    "type": os.environ.get("FIREBASE_TYPE"),
    "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
    "private_key_id": str(os.environ.get("FIREBASE_PRIVATE_KEY_ID")),
    "private_key": str(os.environ.get("FIREBASE_PRIVATE_KEY")).replace(r'\n', '\n'),
    "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
    "auth_uri": os.environ.get("FIREBASE_AUTH_URI"),
    "token_uri": os.environ.get("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.environ.get("FIREBASE_auth_provider_x509_cert_url"),
    "client_x509_cert_url": os.environ.get("FIREBASE_client_x509_cert_url"),
})

firebase_admin.initialize_app(cred)

# run the app.
if __name__ == "__main__":

    
    application.debug = True
    uvicorn.run(application)
