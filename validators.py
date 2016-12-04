from validate_email import validate_email

from utils import form_validators

ERRORS = {
    'required': 'This field is required',
    'email': 'Invalid email format',
    'password_length': 'Minimum password length is 6 signs',
    'passwords_mismatch': 'Passwords are not the same',
    'passwords_not_filled': 'Fill all passwords'
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
    if email and not validate_email(email):
        errors['email'] = ERRORS['email']
    if not password:
        errors['password'] = ERRORS['required']
    if password and len(password) < 6:
        errors['password'] = ERRORS['password_length']
    return errors


class RegisterFormValidator(form_validators.BaseFormValidator):

    def validate_form(self, form):
        username = form.username.text
        email = form.email.text
        password = form.password.text
        errors = register_validator(username, email, password)
        return errors


def settings_validator(old_password, new_password, password_confirm, email):
    errors = {}
    if any([old_password, new_password, password_confirm]) and not all([old_password, new_password, password_confirm]):
        if not old_password:
            errors['old_password'] = ERRORS['passwords_not_filled']
        if not new_password:
            errors['new_password'] = ERRORS['passwords_not_filled']
        if not password_confirm:
            errors['password_confirm'] = ERRORS['passwords_not_filled']

    if old_password and new_password != password_confirm:
        errors['new_password'] = ERRORS['passwords_mismatch']
        errors['password_confirm'] = ERRORS['passwords_mismatch']

    if new_password and len(new_password) < 6:
        errors['new_password'] = ERRORS['password_length']

    if not email:
        errors['email'] = ERRORS['required']

    if email and not validate_email(email):
        errors['email'] = ERRORS['email']
    return errors


class SettingsFormValidator(form_validators.BaseFormValidator):

    def validate_form(self, form):
        old_password = form.old_password.text
        new_password = form.new_password.text
        password_confirm = form.password_confirm.text
        email = form.email.text
        errors = settings_validator(old_password, new_password, password_confirm, email)
        return errors