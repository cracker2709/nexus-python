from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField


class NexusForm(FlaskForm):
    group = StringField('group')  # , validators=[InputRequired("Please fill group name")])
    artifact = StringField('artifact')
    version = StringField('version')
    extension = StringField('extension')
    target_api = HiddenField(default="/")
    submit = SubmitField(label='Search')
    submit_new = SubmitField(label='Search New page')

