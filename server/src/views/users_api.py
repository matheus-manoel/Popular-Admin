from flask import Blueprint
from datetime import datetime

from .responses import build_response, missing_required_payload_parameter
from .utils import get_missing_params


def decode_datetime(obj):
    if isinstance(obj, datetime):
        return int(obj.timestamp())
    raise TypeError("Type %s not serializable." % type(obj))


def create_users_api_views(handlers, request):
    bp = Blueprint('users_api_v1', __name__)

    @bp.route('/', methods=['GET', 'POST'])
    def users():
        if request.method == 'GET':
            return get_users(handlers, request)
        elif request.method == 'POST':
            return post_users(handlers, request)

    return bp


def get_users(handlers, request):
    users = handlers.user.get().to_json()
    return build_response(users)


def post_users(handlers, request):
    obligatory_params = ['name', 'username', 'password', 'email', 'role']
    if get_missing_params(request.args, obligatory_params):
        return missing_required_payload_parameter()
