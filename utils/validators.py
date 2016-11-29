class ValidationError(Exception):
    pass

ERRORS = {
    'required': 'This field is required'
}


def login_validator(username, password):
    errors = {}
    if not username:
        errors['username'] = ERRORS['required']
    if not password:
        errors['password'] = ERRORS['required']

    return errors