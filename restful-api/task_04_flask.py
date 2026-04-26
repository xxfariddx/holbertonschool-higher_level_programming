from flask import Flask, jsonify, request

app = Flask(__name__)

# -----------------------------
# In-memory users database
# -----------------------------
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}

# -----------------------------
# Root endpoint
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


# -----------------------------
# /data endpoint (list usernames)
# -----------------------------
@app.route("/data", methods=["GET"])
def get_usernames():
    return jsonify(list(users.keys()))


# -----------------------------
# /status endpoint
# -----------------------------
@app.route("/status", methods=["GET"])
def status():
    return "OK"


# -----------------------------
# /users/<username> endpoint
# -----------------------------
@app.route("/users/<username>", methods=["GET"])
def get_user(username):

    if username in users:
        return jsonify(users[username])

    return jsonify({"error": "User not found"}), 404


# -----------------------------
# /add_user endpoint (POST)
# -----------------------------
@app.route("/add_user", methods=["POST"])
def add_user():

    # Check if JSON is valid
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check username exists in request
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Check duplicate user
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Create new user
    new_user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=False)
