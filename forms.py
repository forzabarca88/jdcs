from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField(label='Contact Name', validators=[DataRequired()])
    email = StringField(label='Contact Email', validators=[Email(), DataRequired()])
    comment = TextAreaField(label='Comments', validators=[DataRequired()])
    submit = SubmitField(label='Submit')