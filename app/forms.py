from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TicketForm(FlaskForm):
    requester = StringField('Name', validators=[DataRequired()])
    request = StringField('Describe your problem', validators=[DataRequired()])
    urgency = BooleanField('Urgent?')
    submit = SubmitField('submit')
