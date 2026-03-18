from flask import Blueprint, request, jsonify
from services.game_service import GameService

game_bp = Blueprint("game", __name__)

@game_bp.route("/start", methods=["POST"])
def start():
    user_id = request.json["user_id"]
    game = GameService.start_game(user_id)
    return jsonify({"game_id": game.id})

@game_bp.route("/attempt", methods=["POST"])
def attempt():
    data = request.json
    result = GameService.make_attempt(
        data["game_id"],
        data["guess"]
    )
    return jsonify(result)