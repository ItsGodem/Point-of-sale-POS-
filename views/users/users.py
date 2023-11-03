import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from app.users import *
from kivy.clock import Clock, mainthread

from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty,ObjectProperty

Builder.load_file('views/users/users.kv')
class Users(BoxLayout):
    s = []
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        for x in users:
            user={
                'user': x['user'],
                'pass': x['pass']
            }
            self.s.append(user["user"])
            self.users(user)
    def chead(self):
        name = self.ids
    def users(self, user: dict):
        grid = self.ids.gl_users
        pt = User()

        pt.name = user.get('user', '')
        pt.pwd = user.get('pass', '')
        pt.dl = self.del_it
        grid.add_widget(pt)

    def add(self,d= False):
        a = Addu()
        if d == True:
            a.open()
            a.naword = self.naword
    def naword(self,text):
        if not text['user'] in self.s:
            print(text,self.s)
            user = {
                'user': text['user'],
                'pass': text['pass'],
            }
            self.users(user)
            filename = 'app/users.json'
            users.append(user)
            self.s.append(user['user'])
            # 1. Read file contents
            with open(filename, "r") as file:
                data = json.load(file)

            # 2. Update json object
            data.append(user)

            # 3. Write json file
            with open(filename, "w") as file:
                json.dump(data, file)
        
    def del_it(self,tile,name,pwd):
        if name !='root':
            p ={'user': name, 'pass': pwd}
            print(p)
            grid = self.ids.gl_users
            grid.remove_widget(tile)
            users.remove(p)
            self.s.append(p['user'])
            # 1. Read file contents
            with open(filename, "r") as file:
                data = json.load(file)

            # 2. Update json object
            data.remove(p)

            # 3. Write json file
            with open(filename, "w") as file:
                json.dump(data, file)
class Addu(ModalView):

    chead= ObjectProperty(allownone= True)
    naword= ObjectProperty(allownone= True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    def get(self):
        flme= self.ids.si_user.text
        pwd = self.ids.si_pwd.text
        user = {
                'user': flme,
                'pass': pwd,
            }
        return user
        
class User(ButtonBehavior,BoxLayout):
    name = StringProperty('')
    pwd = StringProperty('')
    dl= ObjectProperty(allownone= True)
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    