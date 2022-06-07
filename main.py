# IMPORTS
import sys
import kivy
from kivy.app import App
from widget.welcome import WidgetWelcome
from widget.info_line import WidgetInfoLine


# CLASSES

# Shop ready
class ShopReady(App):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize kivy app
        super().__init__(**kwargs)


    # METHODS

    # Build
    def build(self):
        return WidgetWelcome()


# FUNCTIONS

# Main
def main(args: list[str]):

    # Initialize kivy
    kivy.require("2.1.0")

    # Initialize the application
    app = ShopReady()

    # Run the application
    app.run()


# MAIN
if __name__ == '__main__':
    main(sys.argv)
