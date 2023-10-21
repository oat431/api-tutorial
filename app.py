from flask import Flask
from routes.hello_world_bp import HelloWorldBlueprint

app = Flask(__name__)

class FlaskApp:
    app.register_blueprint(HelloWorldBlueprint.hello_world)

if __name__ == '__main__':
    app.run()