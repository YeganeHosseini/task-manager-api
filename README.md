
# Task Manager API

## Overview
The **Task Manager API** is a RESTful API built with Flask and Flask-RESTful that allows users to manage tasks. It includes user authentication with JSON Web Tokens (JWT) to protect routes, ensuring only authenticated users can create, retrieve, update, and delete tasks.

## Features
- User Registration
- User Login with JWT Token Generation
- Create, Read, Update, Delete (CRUD) operations for tasks
- JWT-protected routes

## Technologies Used
- Python
- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Postman (for API testing)
- GitHub (for version control)

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create and activate a virtual environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
You need to set up a `JWT_SECRET_KEY` in your `app.py` file for token generation.

Example:
```python
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
```

### 5. Run the Flask application
```bash
python run.py
```

### 6. Test the API
You can test the API using **Postman** or **curl**.

### Example Postman Requests:

#### User Registration:

- **URL**: `POST http://127.0.0.1:5000/register`
- **Body (JSON)**:
  ```json
  {
    "username": "testuser",
    "password": "testpass"
  }
  ```

#### User Login:

- **URL**: `POST http://127.0.0.1:5000/login`
- **Body (JSON)**:
  ```json
  {
    "username": "testuser",
    "password": "testpass"
  }
  ```

#### Create a Task (requires JWT token in the Authorization header):

- **URL**: `POST http://127.0.0.1:5000/task`
- **Headers**:
  - Authorization: `Bearer your_jwt_token_here`
- **Body (JSON)**:
  ```json
  {
    "title": "New Task",
    "description": "This is a new task"
  }
  ```

## Project Structure

```bash
.
├── app.py                   # Main entry point of the Flask app
├── models
│   └── task.py              # Task model (in-memory storage)
├── resources
│   ├── task.py              # Task-related resources (routes and logic)
│   └── user.py              # User registration and login resources
├── run.py                   # Runs the Flask app
├── requirements.txt         # List of dependencies
└── README.md                # Project README file
```

## Future Work (Next Steps)
- **Role-Based Access Control (RBAC)**: Implement roles like `admin` and `user`, where admins have more privileges.
- **Task Deadlines and Prioritization**: Add features for setting task deadlines, priorities, and reminders.
- **Pagination**: Implement pagination for retrieving tasks if the task list becomes large.
- **Database Integration**: Migrate from in-memory task storage to a persistent database like SQLite, PostgreSQL, or MySQL.
- **Task Filtering**: Implement filters to retrieve tasks by completion status, priority, or deadline.
- **User Profile Management**: Add user profile management features where users can update their profile information.

## License
This project is licensed under the MIT License.