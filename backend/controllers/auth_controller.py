from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = AuthService.register(data)
    return jsonify({"id": user.id})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = AuthService.login(data)

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({
        "id": user.id,
        "username": user.username
    })