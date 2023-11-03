
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock, mainthread
from app.users import *
from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty

Builder.load_file('views/auth/auth.kv')
class Auth(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    def cheak(self):
        user=self.ids.user.text
        paw=self.ids.paw.text
        
        for x in range(len(users)):
            if user == ((users[x])['user']) and paw == users[x]['pass'] and ((users[x])['user']) != 'root':
                App.get_running_app().root.ids.scrn_mngr.current = "scrn_product"
            elif user == 'root' :
                App.get_running_app().root.ids.scrn_mngr.current = "scrn_root_product"
            else:
                pass