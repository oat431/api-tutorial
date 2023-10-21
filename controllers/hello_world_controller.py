from flask import jsonify,request

class HelloWorldController:
    @staticmethod
    def hello_world():
        return jsonify({'message':'Hello World'})