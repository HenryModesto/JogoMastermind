from models.user import User
from db import db

class UserRepository:

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()