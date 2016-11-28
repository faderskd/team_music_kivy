from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


Builder.load_file('design/root.kv')


class RootWidget(BoxLayout):
    pass


class NotLoggedBoxLayout(BoxLayout):
    def switch_screen(self, screen):
        self.screen_manager.switch_to(screen)


class TeamMusicApp(App):
    def build(self):
        return RootWidget()

if __name__=='__main__':
    TeamMusicApp().run()
