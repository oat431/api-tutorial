from flask import request
from services.user_service import UserService

class UserController:
    @staticmethod
    def get_users():
        return UserService.get_users()
    
    @staticmethod
    def get_user(id:int):
        return UserService.get_user(id)