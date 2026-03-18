from models.game import Game
from db import db

class GameRepository:

    @staticmethod
    def create(game):
        db.session.add(game)
        db.session.commit()
        return game

    @staticmethod
    def find_by_id(game_id):
        return Game.query.get(game_id)

    @staticmethod
    def update():
        db.session.commit()