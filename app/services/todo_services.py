from config import DB_CONFIG
from app.models import create_todo_query, get_todo_query, update_todo_query, delete_todo_query
# we can use here * all instead of writing all functions name

# create todo data
def create_todo(user_id, data):
    try:
        with DB_CONFIG.cursor() as cursor:
            values = (data["title"], data["description"], data["status"], data["priority"], user_id)
            cursor.execute(create_todo_query(), values)
            DB_CONFIG.commit()
            # Returns the ID of the newly created user (auto-incremented primary key).
            return cursor.lastrowid  
    except Exception as e:
        print("error:In creating todo")
        return None

# read todo data
def get_todo(user_id):
    try:
        with DB_CONFIG.cursor() as cursor:
            cursor.execute(get_todo_query(), user_id)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print("error:user_id not found")
        return None

# update todo data
def update_todo(user_id, todo_id, data):
    try:
        with DB_CONFIG.cursor() as cursor:
            values = (data["title"], data["description"], data["status"], data["priority"],user_id,todo_id)
            cursor.execute(update_todo_query(), values)
            DB_CONFIG.commit()
            # it will show the no. of row updated
            return cursor.rowcount
    except Exception as e:
        print("error:something went wrong")
        return None

# delete todo
def delete_todo(user_id, todo_id):
    try:
        with DB_CONFIG.cursor() as cursor:
            cursor.execute(delete_todo_query(), (user_id, todo_id))
            DB_CONFIG.commit()
            return cursor.rowcount
    except Exception as e:
        print("error:something went wrong")
        return None

