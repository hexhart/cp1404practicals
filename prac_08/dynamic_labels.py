"""
CP1404/CP5632 Practical 8 By Hexon Hartley Jimenez
Dynamic Labels App
Estimated Time: 30 Minutes
Actual Time: 55 Minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label

# from kivy.properties import StringProperty

__author__ = 'Hexon Hartley Jimenez'


class DynamicNamesApp(App):
    """Main class - Kivy app to demo the dynamic labels program."""

    # dynamic_name = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)

        # Define the list of names (this is the data or model)
        self.names_to_label = ['Ariana Grande', 'Hayley Williams', 'Miley Cyrus', 'Mariah Carey', 'Taylor Swift']

    def build(self):
        """Build the Kivy GUI"""
        Window.size = (750, 450)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        # self.create_widgets()

        for name in self.names_to_label:
            name_label = Label(text=name)
            self.root.ids.entries_label.add_widget(name_label)

        return self.root

    # Commented out the test code below
    # Initially the code follows through the similar integration with dynamic_widgets
    # But dynamically stripped down some of the feature to follow the task instructions.
    # def create_widgets(self):
    #     """Create labels from data and add them to the GUI."""
    #
    # def press_entry(self, instance):
    #     """Event handles for pressing labels"""
    #     name = instance.text
    #     self.dynamic_name = f"{name} = {self.names_to_label[self.names_to_label.index(name)]}"


DynamicNamesApp().run()
