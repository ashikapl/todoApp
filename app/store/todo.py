from config import DB_CONFIG
from app.models.todo import Todo
# we can use here * all instead of writing all functions name

# create todo data
def add_todo_store(user_id, data):
    with DB_CONFIG.cursor() as cursor:
        query = "INSERT INTO Todo(title, description, status, priority,user_id) VALUES (%s, %s, %s, %s, %s)"
        values = (data["title"], data["description"], data["status"], data["priority"], user_id)
        cursor.execute(query, values)
        DB_CONFIG.commit()
        # Returns the ID of the newly created user (auto-incremented primarykey).
        return cursor.lastrowid  

# read todo data
def get_todo_store(user_id):
    with DB_CONFIG.cursor() as cursor:
        cursor.execute("SELECT * FROM Todo WHERE user_id = %s", user_id)
        result = cursor.fetchall()
        return result

# update todo data
def update_todo_store(user_id, todo_id, data):
    with DB_CONFIG.cursor() as cursor:
        query = "UPDATE Todo SET title=%s, description=%s, status=%s,priority=%s WHERE user_id=%s AND todo_id=%s"
        values = (data["title"], data["description"], data["status"], data["priority"],user_id,todo_id)
        cursor.execute(query, values)
        DB_CONFIG.commit()
        # it will show the no. of row updated
        return cursor.rowcount

# delete todo
def delete_todo_store(user_id, todo_id):
    with DB_CONFIG.cursor() as cursor:
        cursor.execute("DELETE FROM Todo WHERE user_id=%s AND todo_id=%s",(user_id, todo_id))
        DB_CONFIG.commit()
        return cursor.rowcount