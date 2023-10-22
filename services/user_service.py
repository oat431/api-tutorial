from flask import jsonify,request
from models.user import User
from payload.response.user_dto import UserDto

class UserService:
    def create_user():
        return {'message':'Create User'}
    
    def get_user():
        return jsonify({'message':'Get User'})

    def get_users():
        users = []
        user1 = User('John','Doe','oat431@email1.com',21)
        user2 = User('Jane','Doe','oat432@email1.com',22)
        user3 = User('Cat', 'Caties', 'oat433@email1', 24)

        userDto1 = UserDto(user1)
        userDto2 = UserDto(user2)
        userDto3 = UserDto(user3)

        users.append(userDto1.serialize)
        users.append(userDto2.serialize)
        users.append(userDto3.serialize)
        return jsonify(users)
    
    def update_user():
        return jsonify({'message':'Update User'})
    
    def delete_user():
        return jsonify({'message':'Delete User'})