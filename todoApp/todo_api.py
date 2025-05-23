from flask import Flask, request, jsonify
from dotenv import load_dotenv
import pymysql
import os

# Load environment variables
load_dotenv()

todo_api = Flask(__name__)

# Connect to todo database
todo_db = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

todo_cursor = todo_db.cursor()

#------------------------------todo crud api-----------------------------------
# create todo data
@todo_api.route("/todos/<int:user_id>", methods=["POST"])
def create_todo(user_id):
    data = request.get_json()
    query = "INSERT INTO todo_table(title, description, status, priority, user_id) VALUES (%s, %s, %s, %s, %s)"
    values = (data["title"], data["description"], data["status"], data["priority"], user_id)
    todo_cursor.execute(query, values)
    todo_db.commit()
    return jsonify({"message":"Todo Created!"}), 202

# Get method 2 (by using user id)
@todo_api.route("/todos/<int:user_id>", methods=["GET"])
def read_todo2(user_id):
    todo_cursor.execute("SELECT * FROM todo_table WHERE user_id = %s", (user_id))
    user = todo_cursor.fetchall()
    return jsonify(user)

# Update todo data 
@todo_api.route("/todos/<int:user_id>/<int:todo_id>", methods=["PUT"])
def update_todo(user_id, todo_id):
    data = request.get_json()
    query = "UPDATE todo_table SET title=%s, description=%s, status=%s, priority=%s WHERE user_id=%s AND todo_id=%s"
    values = (data["title"], data["description"], data["status"], data["priority"], user_id, todo_id)
    todo_cursor.execute(query,values)
    todo_db.commit()
    return jsonify({"message":"Todo Updated!"}), 200

# Delete todo data
@todo_api.route("/todos/<int:user_id>/<int:todo_id>", methods=["DELETE"])
def delete_todo(user_id, todo_id):
    todo_cursor.execute("SELECT * FROM todo_table WHERE user_id=%s AND todo_id=%s", (user_id, todo_id))
    todo = todo_cursor.fetchone()

    if not todo:
        return jsonify({"message":"Todo Not Found!"}), 404
    
    todo_cursor.execute("DELETE FROM todo_table WHERE user_id=%s AND todo_id=%s", (user_id, todo_id))
    todo_db.commit()
    return jsonify({"message":"Todo Deleted!"}), 200

if __name__ == "__main__":
    todo_api.run(port=5000, debug=True)

