from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name_label = 'Contact Name'
    email_label = 'Contact Email'
    comment_label = 'Comments'
    submit_label = 'Submit'
    name = StringField(label=name_label, 
            validators=[DataRequired('{} is empty.'.format(name_label))])
    email = StringField(label=email_label, validators=[Email('{} must be a\
            valid email address.'.format(email_label)), 
            DataRequired('{} is empty.'.format(email_label))])
    comment = TextAreaField(label=comment_label, 
            validators=[DataRequired('{} is empty.'.format(comment_label))])
    submit = SubmitField(label=submit_label)