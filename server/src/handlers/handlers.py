class UserHandler(object):

    def __init__(self, models):
        self.models = models

    def create_new(self, user_dict):
        user_model = self.models.user

        user_to_add = user_model(
            id=user_dict['id']
        )
        user_to_add.save()

        return user_to_add



