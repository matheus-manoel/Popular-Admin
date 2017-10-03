from ..utils import dotdict
from .handlers import UserHandler, MeetingHandler, TaskHandler


def create_handlers(models):
    return dotdict({
        'user': UserHandler(models),
        'meeting': MeetingHandler(models),
        'task': TaskHandler(models)
    })
