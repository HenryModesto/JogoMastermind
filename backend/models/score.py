from db import db

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)

    attempts = db.Column(db.Integer)   
    time_spent = db.Column(db.Float)   