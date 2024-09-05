# resources/user.py

from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import User, users

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
    parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")

    def post(self):
        data = UserRegister.parser.parse_args()

        if any(user.username == data['username'] for user in users):
            return {"message": "User already exists"}, 400

        user = User(data['username'], data['password'])
        users.append(user)
        return {"message": "User created successfully"}, 201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Username cannot be blank!")
    parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")

    def post(self):
        data = UserLogin.parser.parse_args()

        user = next((user for user in users if user.username == data['username']), None)
        if user and user.verify_password(data['password']):
            access_token = create_access_token(identity=user.username)
            return {"access_token": access_token}, 200

        return {"message": "Invalid credentials"}, 401
