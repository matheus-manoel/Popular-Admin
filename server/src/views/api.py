from flask import Blueprint
from datetime import datetime

from .responses import success


def decode_datetime(obj):
    if isinstance(obj, datetime):
        return int(obj.timestamp())
    raise TypeError("Type %s not serializable." % type(obj))


def create_api_views(handlers, request):
    bp = Blueprint('api_v1', __name__)

    @bp.route('/', methods=['GET'])
    def index():
        return success()

    return bp
