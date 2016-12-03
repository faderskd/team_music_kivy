from utils import request_handlers


class LoginFormHandler(request_handlers.BaseRequestHandler):
    def get_request_data(self, form):
        return {
            'username': form.username.text,
            'password': form.password.text
        }

    def on_success(self, req, result, form):
        root_widget = form.root_widget
        root_widget.set_logged_layout()


class RegisterFormHandler(request_handlers.BaseRequestHandler):
    def get_request_data(self, form):
        return {
            'username': form.username.text,
            'email': form.email.text,
            'password': form.password.text
        }
