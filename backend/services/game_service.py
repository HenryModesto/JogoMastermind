import random
from models.game import Game
from repositories.game_repository import GameRepository

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

        GameRepository.update()

        return {
            "correct": correct,
            "attempts": attempts,
            "finished": game.finished
        }