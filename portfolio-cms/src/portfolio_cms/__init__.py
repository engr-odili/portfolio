import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # type: ignore[import-untyped]
from flask_login import LoginManager  # type: ignore[import-untyped]
from typing import Any
from dotenv import load_dotenv
from pathlib import Path

db: Any = SQLAlchemy()
migrate: Any = Migrate()
login_manager: Any = LoginManager()
env_path: Path = Path(".env")
load_dotenv(dotenv_path=env_path)


def create_app(config: Any = None) -> Any:
    app: Any = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get(
            "SQLALCHEMY_TRACK_MODIFICATIONS"
            )
    )
    if config:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # TODO: Register blueprints here
    # from .admin import admin_bp
    # app.register_blueprint(admin_bp)

    @app.route('/')
    def home():
        return 'HOME PAGE'

    return app
