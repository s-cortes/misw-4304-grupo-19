from flask import Blueprint, request, Response

black_list_bp = Blueprint('blacklist', __name__)
@black_list_bp.route('/blacklists', methods=['POST'])
def create() -> Response:
    pass

@black_list_bp.route('/blacklists/<string:email>', methods=['GET'])
def consult() -> Response:
    pass
