# IMPORTS
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty


# CLASSES

# Info line widget
class WidgetInfoLine(BoxLayout):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize widget
        super().__init__(**kwargs)


# Multi toggle button widget
class WidgetMultiToggleButton(BoxLayout, ToggleButton):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize widget
        super().__init__(**kwargs)


# Error Popup
class WidgetErrorPopup(Popup):

    # CONSTRUCTOR
    def __init__(self, title: str, message1: str, message2: str, **kwargs):

        # Set title and messages
        self.title = title
        self.message1 = message1
        self.message2 = message2

        # Initialize widget
        super().__init__(**kwargs)


# Confirm Popup
class WidgetConfirmPopup(Popup):

    # CONSTRUCTOR
    def __init__(self, title: str, message1: str, message2: str, yes_method, yes_args: tuple, **kwargs):

        # Set title and messages
        self.title = title
        self.message1 = message1
        self.message2 = message2

        # Set the yes method and arguments
        self.yes_method = yes_method
        self.yes_args = yes_args

        # Initialize widget
        super().__init__(**kwargs)
