from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

# GET 
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET 
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST 
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = data
    return jsonify({"message": "User created", "user": data}), 201

# PUT 
@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[username].update(data)
    return jsonify({"message": "User updated", "user": users[username]})

# DELETE 
@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    del users[username]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)

