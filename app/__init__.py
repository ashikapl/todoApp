from flask import Flask
from app.api.api import todo_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bp, url_prefix="/todos")
    return app