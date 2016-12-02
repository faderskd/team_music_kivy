from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

import settings
import validators
import handlers


class FormLayout(StackLayout):
    pass


class RegisterForm(FormLayout):
    def register(self):
        form_validator = validators.RegisterFormValidator(self)
        form_handler = handlers.RegisterFormHandler(
            url=settings.API_URLS['register'],
            form=self,
            method='POST'
        )
        if form_validator.form_is_valid():
            form_handler.send_request()


class LoginForm(FormLayout):
    def login(self):
        form_validator = validators.LoginFormValidator(self)
        form_handler = handlers.LoginFormHandler(
            url=settings.API_URLS['login'],
            form=self,
            method='POST'
        )
        if form_validator.form_is_valid():
            form_handler.send_request()


class RootWidget(BoxLayout):
    pass


class ErrorLabel(Label):
    pass


Builder.load_file('design/root.kv')

Factory.register('ErrorLabel', cls=ErrorLabel)


class TeamMusicApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    TeamMusicApp().run()
