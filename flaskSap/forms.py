from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PersonaForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lastName = StringField('LastName')
    email = StringField('Email', validators=[DataRequired()])
    send = SubmitField('Send')