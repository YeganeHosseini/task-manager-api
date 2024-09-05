# app.py
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, UserLogin
from resources.task import TaskResource, TaskList

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

api = Api(app)
jwt = JWTManager(app)

# Import resources


# Register resources
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(TaskResource, '/task', '/task/<int:task_id>')  # Handles individual tasks
api.add_resource(TaskList, '/tasks')  # Handles list of all tasks


if __name__ == '__main__':
    app.run(debug=True)
