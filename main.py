from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        return GridLayout()


MainApp().run()