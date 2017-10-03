def create_user_model(me):
    class User(me.Document):
        id = me.IntField(primary_key=True)
    return User
