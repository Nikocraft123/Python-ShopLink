# IMPORTS
from kivy.uix.boxlayout import BoxLayout
from main import ShopLink


# CLASSES

# Welcome widget
class WidgetWelcome(BoxLayout):

    # CONSTRUCTOR
    def __init__(self, app: ShopLink, **kwargs):

        # Set the application
        self.app = app

        # Initialize widget
        super().__init__(**kwargs)


    # METHODS

    # On button get started released
    def button_get_started(self):
        print("Get started")
