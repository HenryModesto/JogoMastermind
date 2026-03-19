from flask import Blueprint, request, jsonify
from models.game import Game
from models.score import Score
from db import db
import random
import time

from utils.game_logic import calculate_feedback

game_bp = Blueprint('game', __name__)



@game_bp.route('/start', methods=['POST'])
def start_game():
    data = request.json

    user_id = data.get('user_id')

    colors = ['r', 'b', 'g', 'y']
    secret = ''.join(random.choice(colors) for _ in range(4))

    game = Game(
        user_id=user_id,
        secret_code=secret,
        attempts="[]",
        attempts_count=0,
        finished=False,
        start_time=time.time()
    )

    db.session.add(game)
    db.session.commit()

    return jsonify({"message": "Jogo iniciado"})


@game_bp.route('/attempt', methods=['POST'])
def attempt():
    data = request.json

    user_id = data.get('user_id')
    guess = data.get('guess')

    game = Game.query.filter_by(user_id=user_id, finished=False).first()

    if not game:
        return jsonify({"error": "Nenhum jogo ativo"}), 404

    black, white = calculate_feedback(game.secret_code, guess)

    attempts = game.get_attempts()
    attempts.append({
        "guess": guess,
        "black": black,
        "white": white
    })

    game.set_attempts(attempts)
    game.attempts_count += 1

    finished = False
    won = False

    if black == 4:
        finished = True
        won = True
        game.finished = True
        game.end_time = time.time()

        time_spent = game.end_time - game.start_time

        score = Score(
            user_id=user_id,
            attempts=game.attempts_count,
            time_spent=time_spent
        )

        db.session.add(score)

    elif game.attempts_count >= 10:
        finished = True
        game.finished = True
        game.end_time = time.time()

    db.session.commit()

    return jsonify({
        "black": black,
        "white": white,
        "finished": finished,
        "won": won,
        "secret": game.secret_code if finished else None
    })

@game_bp.route('/ranking', methods=['GET'])
def ranking():

    scores = Score.query.order_by(
        Score.attempts.asc(),
        Score.time_spent.asc()
    ).limit(10).all()

    result = []

    for s in scores:
        result.append({
            "user_id": s.user_id,
            "attempts": s.attempts,
            "time": round(s.time_spent, 2)
        })

    return jsonify(result)