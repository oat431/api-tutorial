from flask import request
from services.user_service import UserService
from payload.request.user_request import UserRequest

class UserController:
    @staticmethod
    def get_users():
        return UserService.get_users()
    
    @staticmethod
    def get_user(id:int):
        return UserService.get_user(id)
    
    @staticmethod
    def create_user():
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email = request.json['email']
        birth_date = request.json['birth_date']
        user_request = UserRequest(firstname,lastname,email,birth_date)
        return UserService.create_user(user_request)

    @staticmethod
    def update_user(id:int):
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        email = request.json['email']
        birth_date = request.json['birth_date']
        user_request = UserRequest(firstname,lastname,email,birth_date)
        return UserService.update_user(id,user_request)

    @staticmethod
    def delete_user(id:int):
        return UserService.delete_user(id)