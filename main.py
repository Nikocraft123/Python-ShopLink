# IMPORTS
import sys
import kivy
from kivy.app import App
from constants import *


# CLASSES

# Shop link
class ShopLink(App):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize kivy app
        super().__init__(**kwargs)

        # Define version and author
        self.version = VERSION
        self.author = AUTHOR


    # METHODS

    # Build
    def build(self):
        from widget.welcome import WidgetWelcome
        from widget.info_line import WidgetInfoLine
        from widget.host_address import WidgetHostAddress
        return WidgetWelcome(self)


# FUNCTIONS

# Main
def main(args: list[str]):

    # Initialize kivy
    kivy.require("2.1.0")

    # Initialize the application
    app = ShopLink()

    # Run the application
    app.run()


# MAIN
if __name__ == '__main__':
    main(sys.argv)
