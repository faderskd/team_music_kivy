from utils import request_handlers


class LoginFormHandler(request_handlers.BaseRequestHandler):
    def get_request_data(self, form):
        return {
            'username': form.username.text,
            'password': form.password.text
        }


class RegisterFormHandler(request_handlers.BaseRequestHandler):
    def get_request_data(self, form):
        return {
            'username': form.username.text,
            'email': form.email.text,
            'password': form.password.text
        }