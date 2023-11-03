import widgets.iconfonts as ic
from os.path import dirname, join
from app import MainApp


ic.register(
    "FeatherIcons",
    join(dirname(__file__), "assets/fonts/feather/feather.ttf"),
    join(dirname(__file__), "assets/fonts/feather/feather.fontd"),
    )

MainApp().run()