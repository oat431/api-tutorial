from flask import Flask
from routes.hello_world_bp import HelloWorldBlueprint
from routes.user_bp import UserBlueprint

app = Flask(__name__)

class FlaskApp:
    app.register_blueprint(HelloWorldBlueprint.hello_world)
    app.register_blueprint(UserBlueprint.user_bp)

if __name__ == '__main__':
    app.run()