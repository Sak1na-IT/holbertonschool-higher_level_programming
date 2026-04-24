Bütün kodlardakı şərhləri təmizlədim, yalnız tələb olunan funksional kodları və "asdfghjkl" docstring-lərini saxladım.

### `task_04_flask.py`

```python
#!/usr/bin/python3
"""
flask
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    asdfghjkl
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    data
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """
    status
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    username
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    errors
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
