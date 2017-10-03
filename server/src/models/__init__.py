from .user import create_user_model, create_task_model, create_meeting_model


def create_models(me):

    class Models(object):
        user = create_user_model(me)
        meeting = create_meeting_model(me)
        task = create_task_model(me)

    return Models
