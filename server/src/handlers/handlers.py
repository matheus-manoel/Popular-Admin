class UserHandler(object):

    def __init__(self, models):
        self.models = models

    def create_new(self, **user_dict):
        return self.models.user(**user_dict).save()

    def get(self, **filters):
        return self.models.user.objects(**filters)


class TaskHandler(object):

    def __init__(self, models):
        self.models = models

    def create_new(self, **task_dict):
        return self.models.task(**task_dict).save()


class MeetingHandler(object):

    def __init__(self, models):
        self.models = models

    def create_new(self, **meeting_dict):
        return self.meeting.create_new(**meeting_dict)
