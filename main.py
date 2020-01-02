from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView

from kivy.properties import StringProperty

class SideBar(BoxLayout):
    pass

class ScrollabelLabel(ScrollView):
    text = StringProperty('')

class HomeScreen(Screen):
    pass

class AboutMeScreen(Screen):
    pass

class TheScreenManager(ScreenManager):
    pass

class BasicApp(App):
    def build(self):
        return 

if __name__=='__main__':
    BasicApp().run()