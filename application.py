from app.auth.security import get_api_key
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
import uvicorn  # optional if you run it directly from terminal
from app.main.routes import mainRouter
from app.agents.routes import agentsRouter
from app.llmTools.routes import llmToolsRouter

application = app = FastAPI()

# Register blueprints here
# from app.agents import bp as agents_bp
# application.register_blueprint(agents_bp, url_prefix='/agents')

# from app.main import bp as main_bp
# application.register_blueprint(main_bp)

@app.get("/test", response_class=PlainTextResponse)
async def hello():
    return "Hello World!"


application.include_router(agentsRouter, prefix="/agents", dependencies=[Depends(get_api_key)])
application.include_router(llmToolsRouter, prefix="/llmTools", dependencies=[Depends(get_api_key)])
application.include_router(mainRouter, prefix="/main", dependencies=[Depends(get_api_key)])

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.timeout_keep_alive=10000
    uvicorn.run(application)
