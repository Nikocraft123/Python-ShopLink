# IMPORTS
from kivy.uix.screenmanager import ScreenManager
from constants import *


# CLASSES

# Window manager
class WindowManager(ScreenManager):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize the window manager
        super().__init__(**kwargs)
