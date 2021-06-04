from flask_wtf import Form
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

class PostForm(Form):
    content = TextAreaField('Content', [validators.Length(min=1, max=280)])
