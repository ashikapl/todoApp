from flask import Flask, jsonify, request, Blueprint
from app.services.todo import *

todo_bp = Blueprint("todo_bp", __name__)

@todo_bp.route("/<int:user_id>", methods=["POST"])
def add_todo(user_id):
    data = request.get_json()
    todo = add_todo_service(user_id,data)
    if "error" in todo:
        return jsonify(todo), 404
    return jsonify({"message":"Todo created", "todo_id":todo["todo_id"]}), 201
    
@todo_bp.route("/<int:user_id>", methods=["GET"])
def get_todo(user_id):
    res = get_todo_service(user_id)
    if "error" in res:
        return jsonify(res), 404
    return jsonify(res), 200
    
@todo_bp.route("/<int:user_id>/<int:todo_id>", methods=["PUT"])
def update_todo(user_id,todo_id):
    data = request.get_json()
    todo = update_todo_service(user_id,todo_id,data)
    if "error" in todo:
        return jsonify(todo), 400
    else:
        return jsonify({"message":"Todo updated"}), 200
        
@todo_bp.route("/<int:user_id>/<int:todo_id>", methods=["DELETE"])
def delete_todo(user_id,todo_id):
    res = delete_todo_service(user_id,todo_id)
    if "error" in res:
        return jsonify(res), 400
    else:
        return jsonify({"message":"Todo deleted"}), 200
        