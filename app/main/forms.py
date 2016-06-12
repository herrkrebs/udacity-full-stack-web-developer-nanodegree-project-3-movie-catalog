from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired


class MovieForm(Form):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description')
    year = IntegerField('year')
    image = URLField('image')
    submit = SubmitField('Submit')
