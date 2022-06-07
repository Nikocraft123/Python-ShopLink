# IMPORTS
from kivy.uix.boxlayout import BoxLayout


# CLASSES

# Host address widget
class WidgetHostAddress(BoxLayout):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize widget
        super().__init__(**kwargs)


    # METHODS

    # On button connect released
    def button_connect(self):
        print("Get started")

