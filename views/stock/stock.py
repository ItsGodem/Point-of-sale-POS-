
import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.modalview import ModalView
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict
from app.users import *
import app.users 
from kivy.clock import Clock, mainthread

from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty,ObjectProperty

Builder.load_file('views/stock/stock.kv')
class Stock(BoxLayout):
    s = []
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        for x in product:
            prod={
                'id': x['id'],
                'name': x['name'],
                'qty': x['qty'],
                'price': x['price']
            }
            self.s.append(prod["name"])
            self.products(prod)
    def chead(self):
        name = self.ids
    def products(self, prod: dict):
        grid = self.ids.gl_users
        pt = Products()

        pt.id = prod.get('id',0)
        pt.name = prod.get('name', '')
        pt.qty = int(prod.get('qty', 0))
        pt.price = float(prod.get('price', 0.00))
        pt.dl = self.del_it
        grid.add_widget(pt)

    def add(self,d= False):
        a = Add()
        if d == True:
            a.open()
            a.naword = self.naword
    def naword(self,text):
        if not text['name'] in self.s:
            print(text,self.s)
            prod={
                'id': text['id'],
                'name': text['name'],
                'qty': text['qty'],
                'price': text['price']
            }
            self.products(prod)
            filename = 'app/product.json'
            product.append(prod)
            self.s.append(prod['name'])
            # 1. Read file contents
            with open(filename, "r") as file:
                data = json.load(file)

            # 2. Update json object
            data.append(prod)

            # 3. Write json file
            with open(filename, "w") as file:
                json.dump(data, file)
        
    def del_it(self,tile):
        p ={'id': tile.id,'name': tile.name, 'qty': tile.qty, 'price': tile.price}
        
        grid = self.ids.gl_users
        grid.remove_widget(tile)
        product.remove(p)
        self.s.append(p['name'])
        # 1. Read file contents
        filename = 'app/product.json'
        with open(filename, "r") as file:
            data = json.load(file)

        # 2. Update json object
        print(p, data)
        data.remove(p)

        # 3. Write json file
        with open(filename, "w") as file:
            json.dump(data, file)
class Add(ModalView):

    chead= ObjectProperty(allownone= True)
    naword= ObjectProperty(allownone= True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    def get(self):
        name= self.ids.si_name.text
        qty= self.ids.si_qty.text
        price = self.ids.si_price.text
        filename = 'app/product.json'
        # 1. Read file contents
        with open(filename, "r") as file:
            data = json.load(file)

        # 2. Update json object
        try:
            prod = {
                    'id': data[-1]['id']+1,
                    'name': name,
                    'qty': int(qty),
                    'price': float(price),
                    }
        except:
            prod = {
                    'id': 0,
                    'name': name,
                    'qty': int(qty),
                    'price': float(price),
                    }
        data.append(prod)
        for x in data:
            product.append(x)
        return prod
        
class Products(ButtonBehavior,BoxLayout):
    id = NumericProperty(0)
    name = StringProperty('')
    qty = NumericProperty(0)
    price = NumericProperty(0.00)
    
    dl= ObjectProperty(allownone= True)
    
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
    
        