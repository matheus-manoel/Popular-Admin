def create_task_model(me):
    class Task(me.Document):
        responsible = me.ListField(me.StringField())
        title = me.StringField()
        description = me.StringField()
        deadline = me.DateTimeField()
        done = me.BooleanField()
    return Task
