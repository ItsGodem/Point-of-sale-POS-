from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from widgets.textfields import FlatField
from kivy.clock import Clock, mainthread
from app.users import *  
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty, ObjectProperty

Builder.load_file('views/roprod/roprod.kv')
class Roprod(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    def w(self):
        
        filename2 = "app/product.json"
        with open(filename2, "r+") as file:
            data = json.load(file)
            for x in data:
                product.append(x)