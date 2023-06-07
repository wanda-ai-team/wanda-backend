from flask import Blueprint

bp = Blueprint('agents', __name__)
from app.agents import routes