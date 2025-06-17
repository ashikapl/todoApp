class Todo:
    def __init__(self, todo_id, title, description, status, priority, user_id):
        self.todo_id = todo_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.user_id = user_id

    def to_dict(self):
        return{
            "todo_id":self.todo_id,
            "title":self.title,
            "description":self.description,
            "status":self.status,
            "priority":self.priority,
            "user_id":self.user_id
        }