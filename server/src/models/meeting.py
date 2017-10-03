def create_meeting_model(me, User):
    class Meeting(me.Document):
        type = me.StringField()
        responsible = me.ListField(me.StringField())
        start = me.DateTimeField()
        end = me.DateTimeField()
        coordinators = me.ListField(me.StringField())
    return Meeting
