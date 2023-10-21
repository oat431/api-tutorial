from flask import Blueprint
from controllers.hello_world_controller import HelloWorldController

class HelloWorldBlueprint:
    hello_world = Blueprint('hello_word',__name__,url_prefix='/hello-world')
    hello_world.route('/',methods=['GET'])(HelloWorldController.hello_world)