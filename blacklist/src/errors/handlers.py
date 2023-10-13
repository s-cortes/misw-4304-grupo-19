from .errors import BaseAPIError

from flask import Response
from http import HTTPStatus
from marshmallow import ValidationError


def handle_api_custom_exception(error: BaseAPIError) -> Response:
    return Response(status=error.code)


def handle_validation_error(error: ValidationError) -> Response:
    return Response(status=HTTPStatus.BAD_REQUEST.value)
