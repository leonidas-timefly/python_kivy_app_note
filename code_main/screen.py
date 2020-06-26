#-*- coding:utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.carousel import Carousel
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ObjectProperty

#from code_main.main import Marvel

class button_press(BoxLayout):
    print("OKKKK")
    textinputtext = StringProperty()
    #def __init__(self, **kwargs):

    def build(self, **kwargs):
        # use a (r, g, b, a) tuple
        print("inside")
        super(button_press, self).__init__(**kwargs)
        self.textinputtext = 'palim'
        start = FloatLayout()

        btn1 = Button(
                     id="first_button",
                     text="button1",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.25, .1),
                     pos_hint={'x': .0, 'y': .0})
        btn1.bind(on_release=button_press.change_button)
        btn2 = Button(
                     id="second_button",
                     text="button2",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.25, .1),
                     pos_hint={'x': .25, 'y': .0})
        btn2.bind(on_release=button_press.change_button)
        btn3 = Button(
                     id="third_button",
                     text="button3",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.25, .1),
                     pos_hint={'x': .50, 'y': .0})
        btn3.bind(on_release=button_press.change_button)
        btn4 = Button(
                     id="forth_button",
                     text="button4",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.25, .1),
                     pos_hint={'x': .75, 'y': .0})
        btn4.bind(on_release=button_press.change_button)
        '''
        self.lbl1 = Label(text="Hello !",
                          font_size=50,
                          color=[0.41, 0.42, 0.74, 1],
                          pos_hint={'x': .0, 'y': .0})
        #original point:(x.center, y.center)
        '''

        self.txt1 = TextInput(text=self.textinputtext,
                              multiline=False,
                              font_size=50,
                              size_hint_y=None,
                              height=100,
                              pos_hint={'x': .0, 'y': .75})
        btn5 = Button(
                     id="ok_button",
                     text="OK",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.25, .1),
                     pos_hint={'x': .38, 'y': .3})
        btn5.bind(on_release=button_press.print_txt(self))
        s = Scatter()
        print(self.txt1.text + "ok")
        start.add_widget(btn1)
        start.add_widget(btn2)
        start.add_widget(btn3)
        start.add_widget(btn4)
        start.add_widget(btn5)
        #start.add_widget(self.lbl1)
        start.add_widget(self.txt1)

        #
        '''
        start.add_widget(s)
        s.add_widget(l)
        s.add_widget(l)
        
        t.bind(text=l.setter('text'))
        '''

        return start

    def change_button(instance):
        print("YES!")
        if instance.id == 'first_button':
            instance.text = "1 pressed"
        elif instance.id == 'second_button':
            instance.text = "2 pressed"
        elif instance.id == 'third_button':
            instance.text = "3 pressed"
        elif instance.id == 'forth_button':
            instance.text = "4 pressed"

    def print_txt(self):
        print(self.textinputtext)



if __name__ == "__main__":
    button_press().run()