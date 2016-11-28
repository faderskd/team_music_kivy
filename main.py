from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('design/root.kv')


class RootWidget(BoxLayout):
    pass


class NotLoggedBoxLayout(BoxLayout):
    def switch_screen(self, screen):
        self.screen_manager.switch_to(screen)


class NotLoggedScreenManager(ScreenManager):
    screen_manager = ObjectProperty(None)


class NotLoggedMainPageScreen(Screen):
    pass


class NotLoggedMenuScreen(Screen):
    screen_manager = ObjectProperty(None)


class LoginForm(Screen):
    pass


class RegisterForm(Screen):
    pass


class TeamMusicApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    TeamMusicApp().run()
