#-*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView
from code_main.screen import button_press
from kivy.uix.textinput import TextInput


'''
class Marvel(BoxLayout):
    def hulk_smash(self):
        self.ids.hulk.text = "hulk: puny god!"
        self.ids["loki"].text = "loki: >_<!!!"

    def button2(self):
        self.button_press.btn.text = "pushed"
'''

class button_event(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return button_press()


class sure_input(App):
    def build(self):
        return text_input.build(App)

if __name__ == '__main__':
    button_event().run()
