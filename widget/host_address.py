# IMPORTS
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from widget.utils import WidgetMultiToggleButton, WidgetErrorPopup, WidgetConfirmPopup


# CLASSES

# Host address select widget
class WidgetHostAddressSelect(Screen):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize widget
        super().__init__(**kwargs)

        # Define the host list
        self.hosts: list[dict[str, str]] = [{"name": "Default", "address": "nikocraftsl.ddns.net", "state": "down"},
                                            {"name": "School", "address": "shoplink.bodensee-gymnasium.de", "state": "normal"},
                                            {"name": "Home", "address": "home.ddns.net", "state": "normal"}]


    # METHODS

    # On entering the screen
    def on_pre_enter(self, *args):

        # Bind the search text update
        self.ids.search.bind(text=self.text_input_search)

        # Update the host list
        self.update_host_list()

    # Update the host list
    def update_host_list(self):

        # Clear old widgets
        self.ids.host_list.clear_widgets()

        # Create new widgets
        for host in self.hosts:
            if host["name"].lower().startswith(self.ids.search.text) or host["address"].lower().startswith(self.ids.search.text):
                host_button = BoxLayout(size_hint_y=None, height="65dp")
                toggle_button = WidgetMultiToggleButton(state=host["state"], on_release=self.toggle_button_host, orientation="vertical")
                toggle_button.add_widget(Label(text=host['name'], font_size="28dp", font_name="fonts/YuGothR.ttc", size_hint_y=1.5))
                toggle_button.add_widget(Label(text=host['address'], font_size="18dp", font_name="fonts/YuGothL.ttc"))
                host_button.add_widget(toggle_button)
                host_button.add_widget(Button(text="X", font_size="28dp", font_name="fonts/YuGothB.ttc",
                                              size_hint_x=None, width="30dp", on_release=self.button_remove_host,
                                              disabled=host["name"] == "Default"))
                self.ids.host_list.add_widget(host_button)

        # Update edit button disabled
        self.ids.edit_button.disabled = False
        for host in self.hosts:
            if host["name"] == "Default" and host["state"] == "down":
                self.ids.edit_button.disabled = True


    # On button connect released
    def button_connect(self, widget: Button):

        # TODO
        print("Connect")
        for host in self.hosts:
            if host["state"] == "down":
                print(host["name"])
                break

    # On button create released
    def button_create(self, widget: Button):

        # Transition to the host address create screen
        self.manager.current = "host_address_create"
        self.manager.transition.direction = "left"

    # On button edit released
    def button_edit(self, widget: Button):

        # Transition to the host address edit screen
        self.manager.current = "host_address_edit"
        self.manager.transition.direction = "left"

        # Set the text inputs
        for host in self.hosts:
            if host["state"] == "down":
                self.manager.screens[3].ids.name.text = host["name"]
                self.manager.screens[3].ids.address.text = host["address"]
                break

    # On text input search type
    def text_input_search(self, widget, text):

        # Update the host list
        self.update_host_list()

    # On button search reset released
    def button_search_reset(self, widget: Button):

        # Reset the search text input
        self.ids.search.text = ""

    # On toggle button host toggle
    def toggle_button_host(self, widget: ToggleButton):

        # Set the toggled host to down and all others to normal
        name = widget.children[1].text
        for host in self.hosts:
            if host["name"] == name:
                host["state"] = "down"
            else:
                host["state"] = "normal"

        # Update the host list
        self.update_host_list()

    # On button remove host released
    def button_remove_host(self, widget: Button):

        # Create and open the confirm popup
        error_popup = WidgetConfirmPopup("Shop Link - Remove Host", "Are you sure, that you want",  f"to remove '{widget.parent.children[1].children[1].text}'!", self.remove_host, (widget,))
        error_popup.open()

    # Remove host
    def remove_host(self, widget: Button):

        # Remove the host
        name = widget.parent.children[1].children[1].text
        select_default = False
        for host in self.hosts:
            if host["name"] == name:
                if host["state"] == "down":
                    select_default = True
                self.hosts.remove(host)
                break

        # If the removed host was selected, select the default host
        if select_default:
            for host in self.hosts:
                if host["name"] == "Default":
                    host["state"] = "down"

        # Update the host list
        self.update_host_list()


# Host address create widget
class WidgetHostAddressCreate(Screen):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize widget
        super().__init__(**kwargs)


    # METHODS

    # On button cancel released
    def button_cancel(self, widget: Button):

        # Transition to the host address select screen
        self.manager.current = "host_address_select"
        self.manager.transition.direction = "right"

        # Reset the text inputs
        self.ids.name.text = ""
        self.ids.address.text = ""

    # On button done released
    def button_done(self, widget: Button):

        # If the name or address text input is empty
        if self.ids.name.text == "" or self.ids.address.text == "":

            # Create and open the error popup
            error_popup = WidgetErrorPopup("Shop Link - Create Host Error", "Cannot create empty host!", "Please fill name and ip!")
            error_popup.open()

            # Return
            return

        # Save the current
        self.manager.screens[1].hosts.insert(1, {"name": self.ids.name.text, "address": self.ids.address.text, "state": "normal"})
        self.manager.screens[1].update_host_list()

        # Reset the text inputs
        self.ids.name.text = ""
        self.ids.address.text = ""

        # Transition to the host address select screen
        self.manager.current = "host_address_select"
        self.manager.transition.direction = "right"


# Host address edit widget
class WidgetHostAddressEdit(Screen):

    # CONSTRUCTOR
    def __init__(self, **kwargs):

        # Initialize widget
        super().__init__(**kwargs)


    # METHODS

    # On button cancel released
    def button_cancel(self, widget: Button):

        # Transition to the host address select screen
        self.manager.current = "host_address_select"
        self.manager.transition.direction = "right"

    # On button done released
    def button_done(self, widget: Button):

        # If the name or address text input is empty
        if self.ids.name.text == "" or self.ids.address.text == "":

            # Create and open the error popup
            error_popup = WidgetErrorPopup("Shop Link - Edit Host Error", "Cannot edit empty host!", "Please fill name and ip!")
            error_popup.open()

            # Return
            return

        # Save the current
        for host in self.manager.screens[1].hosts:
            if host["state"] == "down":
                host["name"] = self.ids.name.text
                host["address"] = self.ids.address.text
        self.manager.screens[1].update_host_list()

        # Transition to the host address select screen
        self.manager.current = "host_address_select"
        self.manager.transition.direction = "right"
