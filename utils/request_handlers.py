import json

from kivy.storage.jsonstore import JsonStore
from kivy.network.urlrequest import UrlRequest

from .form_validators import set_errors_to_form


class BaseRequestHandler(object):
    def __init__(self, url, method, **kwargs):
        self._url = url
        self._method = method
        self._form = kwargs['form'] if 'form' in kwargs else None
        self._async = kwargs['async_req'] if 'async_req' in kwargs else None
        self._success = False

    def _on_success_helper(self, request, result):
        self._success = True
        self.on_success(request, result, self._form)

    def on_success(self, request, result, form):
        pass

    def _on_failure_helper(self, request, error):
        print(error)
        self.on_failure(request, error, self._form)

    def on_failure(self, request, errors, form=None):
        if form:
            set_errors_to_form(form, errors)

    def send_request(self):
        kwargs = {
            'url': self._url,
            'req_headers': self.get_request_headers(),
            'on_success': self._on_success_helper,
            'on_failure': self._on_failure_helper,
            'method': self._method
        }
        data = self.get_request_data(self._form)
        if data:
            json_data = json.dumps(data)
            kwargs['req_body'] = json_data
        if self._async:
            UrlRequest(**kwargs)
        else:
            UrlRequest(**kwargs).wait(0.01)

        return self._success

    def get_request_headers(self):
        store = JsonStore('data.json')
        headers = {'Content-Type': 'application/json'}
        if store.exists('user'):
            token = store.get('user')['token']
            headers['Authorization'] = 'Token %s' % token
        return headers

    def get_request_data(self, form=None):
        return {}