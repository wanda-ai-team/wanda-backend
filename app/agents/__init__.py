from application import application

@application.get("/books")
def get_books():
    # code to return some books
    return {"message": "books"}

from app.agents.routes import * 