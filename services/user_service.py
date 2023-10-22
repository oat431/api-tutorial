from flask import jsonify
from utils.mock_users import MockUser
from payload.request.user_request import UserRequest
from payload.response.user_dto import UserDto
from models.user import User
import datetime

class UserService:
    def create_user(user_request:UserRequest):
        users = MockUser.mock_raw_user()
        new_user = User(
            users.__len__() + 1,
            user_request.firstname,
            user_request.lastname,
            user_request.email,
            user_request.birth_date
        )
        return jsonify(UserDto(new_user).serialize), 201
    
    def get_user(id:int):
        users = MockUser.mock_user()
        for user in users:
            if user['id'] == id:
                return jsonify(user), 200
        return jsonify({'message':'user id:{0} not found'.format(id)}) , 404

    def get_users():
        return jsonify(MockUser.mock_user()), 200
    
    def update_user(id:int, user_request:UserRequest):
        users = MockUser.mock_raw_user()
        update_user = None
        for user in users:
            if user.id == id:
                update_user = user
        
        if update_user is None:
            return jsonify({'message':'user id:{0} not found'.format(id)}) , 404

        update_user.firstname = user_request.firstname
        update_user.lastname = user_request.lastname
        update_user.email = user_request.email
        update_user.birth_date = user_request.birth_date
        resposne = UserDto(user).serialize

        return jsonify(resposne), 200
    
    def delete_user(id:int):
        users = MockUser.mock_raw_user()
        delete_user = None
        for user in users:
            if user.id == id:
                delete_user = user
        
        if delete_user is None:
            return jsonify({'message':'user id:{0} not found'.format(id)}) , 404

        for user in users:
            if user.id == id:
                users.remove(user)
                break
        resposne = []

        for user in users:
            resposne.append(UserDto(user).serialize)

        return jsonify(resposne), 200


