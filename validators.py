from validate_email import validate_email

from utils import form_validators

ERRORS = {
    'required': 'This field is required',
    'email': 'Invalid email format',
    'password': 'Minimum password lengh is 6 signs'
}


def login_validator(username, password):
    errors = {}
    if not username:
        errors['username'] = ERRORS['required']
    if not password:
        errors['password'] = ERRORS['required']

    return errors


class LoginFormValidator(form_validators.BaseFormValidator):

    def validate_form(self, form):
        username = form.username.text
        password = form.password.text
        errors = login_validator(username, password)
        return errors


def register_validator(username, email, password):
    errors = {}
    if not username:
        errors['username'] = ERRORS['required']
    if not email:
        errors['email'] = ERRORS['required']
    if not validate_email(email):
        errors['email'] = ERRORS['email']
    if not password:
        errors['password'] = ERRORS['required']
    if len(password) < 6:
        errors['password'] = ERRORS['password']
    return errors


class RegisterFormValidator(form_validators.BaseFormValidator):

    def validate_form(self, form):
        username = form.username.text
        email = form.email.text
        password = form.password.text
        errors = register_validator(username, email, password)
        return errors
