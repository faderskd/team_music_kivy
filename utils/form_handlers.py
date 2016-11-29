from kivy.factory import Factory

from utils import validators


def login_form_handler(form):
    username = form.username.text
    password = form.password.text

    errors = validators.login_validator(username, password)

    for child in form.children[:]:
        if isinstance(child, Factory.ErrorLabel):
            child.text = ''

    for name, value in errors.items():
        label = getattr(form, name+'_error')
        label.text = value