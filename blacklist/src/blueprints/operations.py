from flask import Blueprint, request, Response
from http import HTTPStatus
from marshmallow import ValidationError
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from errors import DuplicatedError

from models import db, Email, email_schema
from schemas import create_schema

black_list_bp = Blueprint('blacklist', __name__)
@black_list_bp.route('/blacklists', methods=['POST'])
def create() -> Response:
    payload = request.get_json()
    validated_data = create_schema.load(payload)
    try:
        new_email = Email(**validated_data)
        db.session.add(new_email)
        db.session.commit()
    except(IntegrityError, UniqueViolation):
        db.session.rollback()
        raise DuplicatedError()
    return "Email insertado", HTTPStatus.OK.value

@black_list_bp.route('/blacklists/<string:email>', methods=['GET'])
def consult() -> Response:
    pass
