from flask import request
from services.user_service import UserService

class UserController:
    @staticmethod
    def get_users():
        return UserService.get_users()