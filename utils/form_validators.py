from kivy.factory import Factory


def set_errors_to_form(form, errors):
    if 'non_field_errors' in errors:
        non_field_errors = errors.pop('non_field_errors')
        form.non_field_errors.text = non_field_errors[0]

    for name, value in errors.items():
        label = getattr(form, name+'_error')
        label.text = value[0] if isinstance(value, list) else value


def clear_form_errors(form):
    for child in form.children[:]:
        if isinstance(child, Factory.ErrorLabel):
            child.text = ''


class BaseFormValidator(object):
    def __init__(self, form):
        self._form = form
        self._errors = {}

    @property
    def errors(self):
        return self._errors

    def validate_form(self, form):
        errors = {}
        return errors

    def form_is_valid(self):
        clear_form_errors(self._form)

        errors = self.validate_form(self._form)
        if errors:
            set_errors_to_form(self._form, errors)
            self._errors = errors
            return False
        return True