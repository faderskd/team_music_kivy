from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from utils import form_handlers

Builder.load_file('design/root.kv')


class RootWidget(BoxLayout):
    pass


class ErrorLabel(Label):
    pass

Factory.register('ErrorLabel', cls=ErrorLabel)


class NotLoggedBoxLayout(BoxLayout):
    def login(self):
        form = self.login_form
        form_handlers.login_form_handler(form)


class TeamMusicApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    TeamMusicApp().run()
