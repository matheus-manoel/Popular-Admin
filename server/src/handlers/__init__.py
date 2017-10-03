from ..utils import dotdict
from .handlers import UserHandler


def create_handlers(models):
    return dotdict({
        'user': UserHandler(models)
    })
