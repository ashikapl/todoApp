from flask import Flask, jsonify, request, Blueprint
from app.services.todo_services import create_todo, get_todo, update_todo, delete_todo

todo_bp = Blueprint("todo_bp", __name__)

@todo_bp.route("/<int:user_id>", methods=["POST"])
def add_todo(user_id):
    data = request.get_json()
    todo = create_todo(user_id,data)
    if todo:
        return jsonify({"message":"Todo created", "todo_id":todo}), 201
    else:
        return jsonify({"error":"User Not Found"}), 404
    
@todo_bp.route("/<int:user_id>", methods=["GET"])
def read_todo(user_id):
    res = get_todo(user_id)
    if res:
        return jsonify(res), 200
    else:
        return jsonify({"error":"User_id is Invalid"}), 400
    
@todo_bp.route("/<int:user_id>/<int:todo_id>", methods=["PUT"])
def alter_todo(user_id,todo_id):
    data = request.get_json()
    todo = update_todo(user_id,todo_id,data)
    if todo:
        return jsonify({"message":"Todo updated"}), 200
    else:
        return jsonify({"error":"Something went wrong"}), 400
    
@todo_bp.route("/<int:user_id>/<int_todo_id>", methods=["DELETE"])
def del_todo(user_id,todo_id):
    res = delete_todo(user_id,todo_id)
    if res:
        return jsonify({"message":"Todo deleted"}), 200
    else:
        return jsonify({"error":"Something went wrong"}), 400
    
