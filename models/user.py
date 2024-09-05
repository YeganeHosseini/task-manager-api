# models/user.py

from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

# In a real application, you'd store users in a database.
# For simplicity, let's use an in-memory storage for now.
users = []
