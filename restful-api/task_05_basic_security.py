from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

# -----------------------------
# SECRET KEY for JWT
# -----------------------------
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# -----------------------------
# BASIC AUTH SETUP
# -----------------------------
auth = HTTPBasicAuth()

# -----------------------------
# USERS (in-memory)
# -----------------------------
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# -----------------------------
# BASIC AUTH VERIFY FUNCTION
# -----------------------------
@auth.verify_password
def verify(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


# -----------------------------
# BASIC PROTECTED ROUTE
# -----------------------------
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -----------------------------
# LOGIN (JWT TOKEN)
# -----------------------------
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users[username]

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={
        "username": username,
        "role": user["role"]
    })

    return jsonify({"access_token": token}), 200


# -----------------------------
# JWT PROTECTED ROUTE
# -----------------------------
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# -----------------------------
# ADMIN ONLY ROUTE
# -----------------------------
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():

    user = get_jwt_identity()

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -----------------------------
# JWT ERROR HANDLERS (IMPORTANT FOR TESTS)
# -----------------------------
@jwt.unauthorized_loader
def missing_token_callback(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Missing or invalid token"}), 401


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run()
