"""
Example from:
https://kivy.org/doc/stable/guide/basic.html#quickstart
"""

# import
import os
# os.environ["KIVY_WINDOW"] = "pygame"  # {sdl2, pygame, x11, egl_rpi}
# os.environ['KIVY_TEXT'] = 'pil'
import kivy
kivy.logger.Logger.setLevel('DEBUG')
# from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.gridlayout  import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recyclelayout import RecycleLayout

from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.uix.textinput import TextInput
# from kivymd.uix.textinput import MDTextInput

class LoginScreen(GridLayout):
# class LoginScreen(FloatLayout):
# class LoginScreen(RecycleLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(MDLabel(text='User Name'))
        # self.username = TextInput(multiline=False)
        # self.add_widget(self.username)
        self.add_widget(TextInput(multiline=False))
        self.add_widget(MDLabel(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(MDApp):

    def build(self):
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette="Azure"
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()