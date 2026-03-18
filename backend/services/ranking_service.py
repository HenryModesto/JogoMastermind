from models.score import Score

class RankingService:

    @staticmethod
    def get_ranking():
        return Score.query.order_by(Score.points.desc()).all()