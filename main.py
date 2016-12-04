from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.stacklayout import StackLayout
from kivy.storage.jsonstore import JsonStore

import settings
import validators
import handlers


class ErrorLabel(Label):
    pass


class FormLayout(StackLayout):
    pass


class NotLoggedMenu(BoxLayout):
    pass


class NotLoggedNavigator(ScreenManager):
    pass


class LoggedInMenu(BoxLayout):
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


class SettingsForm(FormLayout):
    def change_settings(self):
        store = JsonStore('data.json')
        user_id = store.get('user')['id']
        form_validator = validators.SettingsFormValidator(self)
        form_handler = handlers.SettingsFormHandler(
            url=settings.API_URLS['settings'] + str(user_id) + '/',
            form=self,
            method='PUT'
        )
        if form_validator.form_is_valid():
            form_handler.send_request()


class LoggedInNavigator(ScreenManager):
    def logout(self):
        root_widget = self.root_widget
        root_widget.set_not_logged_layout()
        store = JsonStore('data.json')
        store.delete('user')


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        store = JsonStore('data.json')
        if store.exists('user'):
            token = store.get('user')['token']
            check_token_handler = handlers.CheckTokenHandler(
                url=settings.API_URLS['check_token'] + token,
                method='GET',
                root_widget=self,
                token=token
            )
            check_token_handler.send_request()

    def set_logged_layout(self):
        self.clear_widgets()

        logged_in_menu = Factory.LoggedInMenu()
        logged_in_navigator = LoggedInNavigator()
        logged_in_navigator.root_widget = self
        logged_in_menu.screen_manager = logged_in_navigator
        self.screen_manager = logged_in_navigator
        self.menu = logged_in_menu

        self.add_widget(logged_in_menu)
        self.add_widget(logged_in_navigator)

    def set_not_logged_layout(self):
        self.clear_widgets()

        not_logged_menu = NotLoggedMenu()
        not_logged_navigator = NotLoggedNavigator()
        not_logged_navigator.root_widget = self
        not_logged_menu.screen_manager = not_logged_navigator
        self.screen_manage = not_logged_navigator
        self.menu = not_logged_menu

        self.add_widget(not_logged_menu)
        self.add_widget(not_logged_navigator)


Builder.load_file('design/root.kv')
Builder.load_file('design/common.kv')
Builder.load_file('design/not_logged.kv')
Builder.load_file('design/logged.kv')

Factory.register('ErrorLabel', cls=ErrorLabel)


class TeamMusicApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    TeamMusicApp().run()
