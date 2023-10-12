from dotenv import load_dotenv
from flask import Flask
from marshmallow import ValidationError

from blueprints import black_list_bp
from errors import BaseAPIError, handle_api_custom_exception, handle_validation_error
from models import db, ma
from utils import DatabaseUtil


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DatabaseUtil.generate_database_uri()

    with app.app_context():
        db.init_app(app=app)
        ma.init_app(app=app)
        db.create_all()
    app.register_blueprint(black_list_bp)
    app.register_error_handler(BaseAPIError, handle_api_custom_exception)
    app.register_error_handler(ValidationError, handle_validation_error)
    return app
