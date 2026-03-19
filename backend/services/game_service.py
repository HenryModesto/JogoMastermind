import random
import time
from models.game import Game
from models.score import Score
from repositories.game_repository import GameRepository
from db import db

class GameService:

    @staticmethod
    def generate_code():
        return "".join(str(random.randint(0, 5)) for _ in range(4))

    @staticmethod
    def start_game(user_id):
        game = Game(
            user_id=user_id,
            secret_code=GameService.generate_code()
        )
        return GameRepository.create(game)

    @staticmethod
    def make_attempt(game_id, guess):
        game = GameRepository.find_by_id(game_id)

        if game.finished:
            return {"error": "Game already finished"}

        correct = sum([1 for i in range(4) if guess[i] == game.secret_code[i]])

        attempts = game.get_attempts()
        attempts.append({
            "guess": guess,
            "correct": correct
        })

        game.set_attempts(attempts)
        game.attempts_count += 1

        if correct == 4 or game.attempts_count >= 10:
            game.finished = True
            game.end_time = time.time()

            time_spent = int(game.end_time - game.start_time)
            points = max(0, 100 - (game.attempts_count * 10))

            score = Score(
                user_id=game.user_id,
                points=points,
                time_spent=time_spent
            )

            db.session.add(score)

        GameRepository.update()

        return {
            "correct": correct,
            "attempts": attempts,
            "finished": game.finished
        }