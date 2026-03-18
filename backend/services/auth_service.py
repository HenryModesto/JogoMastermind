from models.user import User
from repositories.user_repository import UserRepository

class AuthService:

    @staticmethod
    def register(data):
        user = User(
            username=data["username"],
            email=data["email"]
        )
        user.set_password(data["password"])
        return UserRepository.create(user)

    @staticmethod
    def login(data):
        user = UserRepository.find_by_username(data["username"])

        if not user or not user.check_password(data["password"]):
            return None

        return user