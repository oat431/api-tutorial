from flask import jsonify
from utils.mock_users import MockUser

class UserService:
    def create_user():
        return {'message':'Create User'}
    
    def get_user(id:int):
        users = MockUser.mock_user()
        for user in users:
            if user['id'] == id:
                return jsonify(user)
        return jsonify({'message':'not found'})

    def get_users():
        return jsonify(MockUser.mock_user())
    
    def update_user():
        return jsonify({'message':'Update User'})
    
    def delete_user():
        return jsonify({'message':'Delete User'})


