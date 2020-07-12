from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from reminder_project.database import DataBase
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivy.uix.checkbox import CheckBox


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()
                Window.clearcolor = (1, 1, 1, 1)
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        Window.clearcolor = (1, 1, 1, 1)
        sm.current = "login"


    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class ChooseInterests(Screen):

    def checkbox_click(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)


    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            Window.clearcolor = (1, 1, 1, 1)
            sm.current = "main"
        else:
            invalidLogin()


    def createBtn(self):
        self.reset()
        Window.clearcolor = (1, 1, 1, 1)
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""


    def logOut(self):
        Window.clearcolor = (1, 1, 1, 1)
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        #Window.clearcolor = (1, 1, 1, 1)
        Window.clearcolor = (0, 0, .30, .60)
        sm.current = "choose"
        '''
        self.n.text = "Account Name:" + name
        self.email.text = "Email:" + self.current
        self.created.text = "Created On: " + created
        '''


class ChatWindow(Screen):
    pass


class ContactWindow(Screen):
    pass


class DiscoverWindow(Screen):
    pass


class MeWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None),
                size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Login',
                content=Label(text='Invalid username or password.'),
                size_hint=(None, None),
                size=(400, 400))
    pop.open()


kv = Builder.load_file("my.kv")
sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"), ChatWindow(name="chat"), ContactWindow(name="contact"), DiscoverWindow(name="discover"), MeWindow(name="me"), ChooseInterests(name="choose")]

for screen in screens:
    sm.add_widget(screen)
Window.clearcolor = (1, 1, 1, 1)
sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()


