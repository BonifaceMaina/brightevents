from wtforms import Form, StringField, PasswordField, validators

class Registrationform(Form):
    name = StringField('Name', [validators.Length(min=4, max=16), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6, max=32), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=6, max=20), validators.DataRequired(), validators.EqualTo('confirm', message='Passwords are not a match')])
    confirm = PasswordField('Confirm Password')

class Loginform(Form):
    email = StringField('Email', [validators.Length(min=6, max=32), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=6, max=20), validators.DataRequired()])
