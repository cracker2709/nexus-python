from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class NexusForm(FlaskForm):
    group = StringField('group')  # , validators=[InputRequired("Please fill group name")])
    artifact = StringField('artifact')
    version = StringField('version')
    extension = StringField('extension')
    submit = SubmitField('Search')
