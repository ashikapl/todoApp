from config import DB_CONFIG
from app.store.todo import *
from app.utils.validator import validate_user
# we can use here * all instead of writing all functions name

user_service_url = "http://127.0.0.1:5000/users"

# create todo data
def add_todo_service(user_id, data):
    try:
        # need to check if user with a particular id if the user exist or not by making user get by id 
        if not validate_user(user_id):
            return {"error":"Invalid User!"}
        
        result = add_todo_store(user_id, data)
        return {"todo_id":result}
    
    except Exception as e:
        return {"error":str(e)}

# read todo data
def get_todo_service(user_id):
    try:
        if not validate_user(user_id):
            return {"error":"Invalid User!"}
        
        result = get_todo_store(user_id)
        return result
    
    except Exception as e:
        return {"error":str(e)}

# update todo data
def update_todo_service(user_id, todo_id, data):
    try:
        if not validate_user(user_id):
            return {"error":"Invalid User!"}
        
        rowCount = update_todo_store(user_id, todo_id, data)
        if rowCount ==  0:
            return {"error":"Todo Not Found!"}
        return {"rowCount":rowCount}
    
    except Exception as e:
        return {"error":str(e)}

# delete todo
def delete_todo_service(user_id, todo_id):
    try:
        if not validate_user(user_id):
            return {"error":"Invalid User!"}
        
        rowCount_delete = delete_todo_store(user_id, todo_id)
        if rowCount_delete == 0:
            return {"error":"Todo Not Found!"}
        return {"rowCount_delete":rowCount_delete}
    
    except Exception as e:
        return {"error":str(e)}

