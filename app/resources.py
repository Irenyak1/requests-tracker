from flask import jsonify, abort, request
from app import app
from app.database import User


@app.route('/api/v1/index', methods = ['GET'])
def index():
    return jsonify({'message': 'Hello World!'}), 200

@app.route('/api/v1/users', methods = ['GET'])
def get_users():
    return User.getUsers()

@app.route('/api/v1/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    return User.getUser(user_id)

@app.route('/api/v1/users', methods = ['POST'])
def create_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    return User.addUser()
