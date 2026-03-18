from flask import Flask
from flask_cors import CORS
from config import Config
from db import db  # 👈 IMPORTA DO DB

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    from controllers.auth_controller import auth_bp
    from controllers.game_controller import game_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(game_bp, url_prefix="/game")

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)