from flask import jsonify, abort, request

class User:
	""" This class provides a way to store user data. """
	users = [
		{
			'id': 1,
			'username': u'mwinel',
			'password': u'123456'
		},
		{
			'id': 2,
			'username': u'lucy',
			'password': u'123456'
		}
	]

	def addUser():
		""" Method to create a new user. """
		user = {
			'id': User.users[-1]['id'] + 1,
			'username': request.json['username'],
			'password': request.json.get('password', "")
		}
		User.users.append(user)
		return jsonify({'user': user}), 201

	def getUser(user_id):
		""" Method to return a single user. """
		user = [user for user in User.users if user['id'] == user_id]
		if len(user) == 0:
			abort(404)
		return jsonify({'user': user[0]})

	def getUsers():
		""" Method to return a list of users. """
		return jsonify({'users': User.users})
