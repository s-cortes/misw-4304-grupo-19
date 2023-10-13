from flask import Blueprint, request, Response
from http import HTTPStatus
from marshmallow import ValidationError
from psycopg2.errors import UniqueViolation
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from errors import DuplicatedError

from models import db, Email, email_schema
from schemas import create_schema
from schemas.serializer import GetEmailResponseSchema

black_list_bp = Blueprint('blacklist', __name__)


@black_list_bp.route('/blacklists', methods=['POST'])
def create() -> tuple[any, int]:
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
def consult(email: str) -> tuple[any, int]:
    """
    Returns a boolean answering whether the email is in the blacklist or not, and the reason why
    :param email:
    :return:
    """
    email: Email = db.session.execute(
        select(Email).where(Email.email == email)
    ).scalar()
    response_schema = GetEmailResponseSchema()
    if email is None:
        return response_schema.dump({
            "exists": False,
            "reason": "No se encuentra en la lista negra"
        }), HTTPStatus.OK.value

    return response_schema.dump({
        "exists": True,
        "reason": email.reason
    }), HTTPStatus.OK.value
