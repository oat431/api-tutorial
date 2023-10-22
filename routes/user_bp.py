from flask import Blueprint
from controllers.user_controller import UserController

class UserBlueprint:
    user_bp = Blueprint('user',__name__,url_prefix='/api/v1/users')

    user_bp.route('/all',methods=['GET'])(UserController.get_users)