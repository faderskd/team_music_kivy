import json

from kivy.network.urlrequest import UrlRequest

from .form_validators import set_errors_to_form


class BaseRequestHandler(object):
    def __init__(self, url, form, method, async_req=False):
        self._url = url
        self._form = form
        self._method = method
        self._async = async_req
        self._success = False

    def _on_success_helper(self, req, result):
        self._success = True
        self.on_success(req, result, self._form)

    def on_success(self, req, result, form):
        pass

    def _on_failure_helper(self, req, error):
        self.on_failure(req, error, self._form)

    def on_failure(self, req, errors, form):
        set_errors_to_form(form, errors)

    def send_request(self):
        data = self.get_request_data(self._form)
        json_data = json.dumps(data)
        kwargs = {
            'url': self._url,
            'req_body': json_data,
            'req_headers': {'Content-Type': 'application/json'},
            'on_success': self._on_success_helper,
            'on_failure': self._on_failure_helper,
            'method': self._method
        }
        if self._async:
            UrlRequest(**kwargs)
        else:
            UrlRequest(**kwargs).wait(0.01)

        return self._success

    def get_request_data(self, form):
        return {}
