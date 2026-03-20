from datetime import datetime
from app.extensions import db

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    secret_code = db.Column(db.String(20), nullable=False) 
    status = db.Column(db.String(20), default='ongoing') 
    attempts_count = db.Column(db.Integer, default=0)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    finished_at = db.Column(db.DateTime, nullable=True)
    duration_seconds = db.Column(db.Integer, nullable=True)

    user = db.relationship('User', back_populates='games')
    attempts = db.relationship('Attempt', back_populates='game', lazy=True, cascade="all, delete-orphan")
