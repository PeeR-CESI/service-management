from flask import Blueprint, jsonify

helloWorld_bp = Blueprint('your_service', __name__)
@helloWorld_bp.route('/')
def hello_world():
    return jsonify({"message": "Hello World"})