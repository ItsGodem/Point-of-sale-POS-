
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


Builder.load_file('views/product/product.kv')
class Product(BoxLayout):
    a = []
    current_cart = []
    item = []
    b= len(product)
    current_total = NumericProperty(0.0)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)
    def render(self, _):
        self.addd()
    def addd(self):
        prods = []
        for x in range(len(product)):
            prod = {
                "name": (product[x])['name'],
                "qty":  (product[x])['qty'],
                "qty2": 1,
                "price": (product[x])['price'],
                'id': (product[x])['id']
            }
            prod2 = {
                'id': (product[x])['id'],
                "name": (product[x])['name'],
                "qty":  1,
                "price": (product[x])['price'],
            }
            prod_se = {
                'name': (product[x])['name'],
                'price': (product[x])['price'],
                'qty': (product[x])['qty'],
                'add': self.add,
                'id': (product[x])['id']
            }
            prods.append(prod_se)
            self.current_cart.append(prod2)
            self.add_Product(prod)

        self.ids.ti_search.choices = prods
    def add_Product(self, product: dict):
        grid = self.ids.container
        pt = ProductTile()

        pt.name = product.get('name', '')
        pt.qty = int(product.get('qty', 0))
        pt.qty2 = int(product.get('qty2', 0))
        pt.price = float(product.get('price', 0.0))

        pt.id = product.get('id', 0)
        pt.add = self.add
        grid.add_widget(pt)
    def qty_control(self, tile, increasing=False):
        _qty = int(tile.qty)
        grid = self.ids.gl_receipt
        _price = int(tile.price)
        if increasing:  
            _qty+=1   
        else:
            if _qty >1:     
                _qty-=1
        tile.qty = _qty
        self.update_total()
    def del_it(self, tile):
        p ={'id': tile.id,'name': tile.name, 'qty': int(tile.qty/tile.qty) ,'price': tile.price }
        
        grid = self.ids.gl_receipt
        grid.remove_widget(tile)
        self.item.remove(p)
        self.update_total()
        if self.b<len(product):
            self.b+=1
    def add(self,id, increasing=False):
        if self.b> 0:
            for x in range(len(product)):
                try:
                    if id == product[x]['id'] and not  self.current_cart[x] in self.item:
                        
                        prod = {
                            'id': (product[x])['id'],
                            "name": (product[x])['name'],
                            "qty":  1,
                            
                            "price": (product[x])['price'],
                            
                        }
                        self.b -=1
                        self.item.append(prod)
                        self.add_item(prod)
                        self.update_total()
                        

                        break   
                    else:
                        continue
                except:
                    prod = {
                        "name": (product[x])['name'],
                        "qty":  1,
                        
                        "price": (product[x])['price'],
                        'id': (product[x])['id']
                    }
                    self.item.append(prod)
                    self.add_item(prod)
                    self.update_total()
                    self.b-=1
                    break   
    def update_total(self):
        prods = self.ids.gl_receipt.children
        _total = 0.0
        for c in prods:
            _total +=(round(float(c.price), 2)* c.qty)
        self.current_total = _total
    def add_item(self, product):
        grid = self.ids.gl_receipt
        
        pt = ReceiptItem()
        pt.qty_callback = self.qty_control
        pt.deli = self.del_it
        pt.name = product.get('name', '')
        pt.qty = int(product.get('qty', 0))
        pt.price = float(product.get('price', 0.0))
        pt.id = product.get('id', 0)
        grid.remove_widget(pt)
        grid.add_widget(pt)

    
        
class ProductTile(ButtonBehavior,BoxLayout):
    id= NumericProperty(0)
    name = StringProperty('')
    qty = NumericProperty(0)
    qty2 = NumericProperty(0)
    price = NumericProperty(0)
    qty_callback = ObjectProperty(allownone= True)
    add = ObjectProperty(allownone= True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass
class ReceiptItem(ButtonBehavior,BoxLayout):
    name = StringProperty('')
    qty = NumericProperty(0)
    price = NumericProperty(0)
    id =  NumericProperty(0)
    qty_callback = ObjectProperty(allownone= True)
    deli = ObjectProperty(allownone= True)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        pass

