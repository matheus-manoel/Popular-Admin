def create_user_model(me):
    class User(me.Document):
        name = me.StringField(required=True)
        username = me.StringField(required=True)
        password = me.StringField(required=True)
        email = me.StringField(required=True)
        role = me.StringField(required=True)
    return User
