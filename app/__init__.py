from flask import Flask
from app.routes.todo_routes import todo_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_bp, url_prefix="/todos")
    return app