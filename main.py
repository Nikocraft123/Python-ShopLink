# INFO
from constants import *
__version__ = VERSION


# IMPORTS
import sys
import os
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from window_manager import WindowManager
from widget.utils import WidgetInfoLine, WidgetMultiToggleButton, WidgetErrorPopup, WidgetConfirmPopup
from widget.welcome import WidgetWelcome
from widget.host_address import WidgetHostAddressSelect


# CLASSES

# Shop link
class ShopLink(App):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize kivy app
        super().__init__(**kwargs)

        # Define version and author
        self.version: str = VERSION
        self.author: str = AUTHOR

        # Set the window title
        self.title: str = "Shop Link"

        # Load the main config file
        if not os.path.exists("./config"):
            os.mkdir("./config")
        self.main_config = JsonStore("./config/main_config.json")


    # METHODS

    # Build
    def build(self):
        wm = WindowManager()
        if not self.main_config.exists("welcome"):
            wm.current = "welcome"
            self.main_config["welcome"] = {}
        else:
            wm.current = "host_address_select"
            wm.transition.direction = "up"
        return wm


# FUNCTIONS

# Main
def main(args):

    # Initialize kivy
    kivy.require("1.9.0")

    # Load kv files
    Builder.load_file("main.kv")

    # Initialize the application
    app: ShopLink = ShopLink()

    # Run the application
    app.run()


# MAIN
if __name__ == '__main__':
    main(sys.argv)
