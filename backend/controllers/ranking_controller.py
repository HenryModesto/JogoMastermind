from models.user import User

class RankingService:

    @staticmethod
    def get_ranking():
        return User.query.order_by(User.best_score.desc()).limit(10).all()