# create todo 
def create_todo_query():
    return """INSERT INTO todo_table(title, description, status, priority, user_id)
              VALUES (%s, %s, %s, %s, %s)"""

# read todo
def get_todo_query():
    return "SELECT * FROM todo_table WHERE user_id = %s"

# update todo
def update_todo_query():
    return """UPDATE todo_table SET title=%s, description=%s, status=%s, priority=%s 
              WHERE user_id=%s AND todo_id=%s"""

# delete todo
def delete_todo_query():
    return "DELETE FROM todo_table WHERE user_id=%s AND todo_id=%s"