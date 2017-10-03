from .user import create_user_model


def create_models(me):

    class Models(object):
        user = create_user_model(me)

    return Models
