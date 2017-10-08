from flask import Blueprint
from datetime import datetime
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from .responses import success, build_response, unauthorized
from .responses import missing_required_payload_parameter
from .utils import get_missing_params


def decode_datetime(obj):
    if isinstance(obj, datetime):
        return int(obj.timestamp())
    raise TypeError("Type %s not serializable." % type(obj))


def create_api_views(handlers, request):
    bp = Blueprint('api_v1', __name__)

    @bp.route('/', methods=['GET'])
    def index():
        return success()

    @bp.route('/protected', methods=['GET'])
    @jwt_required
    def protected():
        current_user = get_jwt_identity()
        return build_response(current_user)

    @bp.route('/login', methods=['POST'])
    def login():
        obligatory_params = ['username', 'password']
        if get_missing_params([*request.form.keys()], obligatory_params):
            return missing_required_payload_parameter()

        given_username = request.form.get('username')
        given_password = request.form.get('password')

        user = handlers.user.get(username=given_username).first()
        if user and user.password == given_password:
            access_token = {'access_token': create_access_token(identity=given_username)}
            return build_response(access_token)
        else:
            return unauthorized()


    return bp
