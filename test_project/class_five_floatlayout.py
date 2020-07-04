import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        return FloatLayout()



if __name__ == "__main__":
    MyApp().run()




'''
<Button>:
    font_size:40
    color:0.3, 0.6, 0.7, 1
    size_hint: 0.3, 0.5


<FloatLayout>:
    Button:
        pos_hint:{"x":0.5, "top":1}
        text:"Tech with"

    Button:
        id: btn
        pos_hint: {"y": 0.3}
        text:"me" if btn.state == "normal" else "Down"
        background_color: 0.3, 0.5, 0.5, 1
'''