# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class ThreadSelectForm(FlaskForm):
    thread = SelectField('Выберите чат', validators=[DataRequired()])
    submit = SubmitField('Открыть чат')

class MessageForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    send = SubmitField('Send')
