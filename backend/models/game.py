from db import db
import json
import time

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)

    secret_code = db.Column(db.String(10), nullable=False)

    attempts = db.Column(db.Text, default="[]")  
    attempts_count = db.Column(db.Integer, default=0)

    finished = db.Column(db.Boolean, default=False)

    start_time = db.Column(db.Float, default=time.time)
    end_time = db.Column(db.Float, nullable=True)

    def set_attempts(self, attempts):
        self.attempts = json.dumps(attempts)

    def get_attempts(self):
        return json.loads(self.attempts)