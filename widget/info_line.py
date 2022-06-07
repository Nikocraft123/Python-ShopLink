# IMPORTS
from kivy.uix.boxlayout import BoxLayout
from constants import *


# CLASSES

# Info line widget
class WidgetInfoLine(BoxLayout):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize widget
        super().__init__(**kwargs)

        # Define version and author
        self.version = VERSION
        self.author = AUTHOR
