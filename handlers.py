from kivy.storage.jsonstore import JsonStore

from utils import request_handlers


class LoginFormHandler(request_handlers.BaseRequestHandler):
    def get_request_data(self, form=None):
        return {
            'username': form.username.text,
            'password': form.password.text
        }

    def on_success(self, req, result, form=None):
        root_widget = form.root_widget
        root_widget.set_logged_layout()

        store = JsonStore('data.json')
        store.put('user', token=result['token'], id=result['id'])


class RegisterFormHandler(request_handlers.BaseRequestHandler):
    def get_request_data(self, form=None):
        return {
            'username': form.username.text,
            'email': form.email.text,
            'password': form.password.text
        }


class CheckTokenHandler(request_handlers.BaseRequestHandler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._token = kwargs['token']
        self._root_widget = kwargs['root_widget']

    def get_request_data(self, form=None):
        return {
            'token': self._token
        }

    def on_success(self, request, result, form):
        self._root_widget.set_logged_layout()


class SettingsFormHandler(request_handlers.BaseRequestHandler):
    def get_request_data(self, form=None):
        data = {
            'email': form.email.text
        }
        old_password = form.old_password.text
        new_password = form.new_password.text
        password_confirm = form.password_confirm.text
        if old_password:
            data['old_password'] = old_password
        if new_password:
            data['new_password1'] = new_password
        if password_confirm:
            data['new_password2'] = password_confirm
        return data