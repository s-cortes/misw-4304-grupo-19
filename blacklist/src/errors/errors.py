from http import HTTPStatus


class BaseAPIError(Exception):
    code = HTTPStatus.INTERNAL_SERVER_ERROR.value
    description = HTTPStatus.INTERNAL_SERVER_ERROR.phrase


class DuplicatedError(BaseAPIError):
    code = HTTPStatus.PRECONDITION_FAILED.value
    description = "El email ya se encuentra en la lista negra"
