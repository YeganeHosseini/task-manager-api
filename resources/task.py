# resources/task.py
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from models.task import Task, tasks

# Handles individual task operations (Create, Get by ID, Update, Delete)
class TaskResource(Resource):
    # Define the parser for request arguments (title and description)
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help="Title cannot be blank!")
    parser.add_argument('description', type=str, required=False)

    # Create a new task
    @jwt_required()
    def post(self):
        data = TaskResource.parser.parse_args()
        task = Task(data['title'], data.get('description'))  # Create new task with parsed data
        task.id = len(tasks) + 1  # Assign a new ID
        tasks.append(task)  # Add the new task to the list
        return {"task": {"id": task.id, "title": task.title, "description": task.description}}, 201

    # Retrieve a task by ID
    @jwt_required()
    def get(self, task_id):
        task = next((task for task in tasks if task.id == task_id), None)  # Find task by ID
        if task:
            return {"task": {"id": task.id, "title": task.title, "description": task.description}}, 200
        return {"message": "Task not found"}, 404

    # Update an existing task by ID
    @jwt_required()
    def put(self, task_id):
        data = TaskResource.parser.parse_args()
        task = next((task for task in tasks if task.id == task_id), None)
        if task:
            task.title = data['title']  # Update title
            task.description = data.get('description')  # Update description
            return {"task": {"id": task.id, "title": task.title, "description": task.description}}, 200
        return {"message": "Task not found"}, 404

    # Delete a task by ID
    @jwt_required()
    def delete(self, task_id):
        global tasks
        tasks = [task for task in tasks if task.id != task_id]  # Remove task from the list
        return {"message": "Task deleted"}, 200


# Handles retrieving the list of all tasks (GET /tasks)
class TaskList(Resource):
    @jwt_required()
    def get(self):
        # Return the list of all tasks with their ID, title, and description
        return {
            "tasks": [
                {"id": task.id, "title": task.title, "description": task.description} for task in tasks
            ]
        }, 200
