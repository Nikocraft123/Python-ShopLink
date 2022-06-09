# IMPORTS
from kivy.uix.screenmanager import Screen


# CLASSES

# Welcome widget
class WidgetWelcome(Screen):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize widget
        super().__init__(**kwargs)


    # METHODS

    # On button get started released
    def button_get_started(self, widget):

        # Transition to the host address select screen
        self.manager.current = "host_address_select"
        self.manager.transition.direction = "left"
