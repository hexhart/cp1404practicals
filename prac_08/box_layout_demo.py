"""
CP1404/CP5632 Practical 8 By Hexon Hartley Jimenez
Modifying Existing GUI Program - box_layout_demo.py
Estimated Time: 30 minutes
Actual Time: 25 minutes
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """This is the main method for loading and showing the program window"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """An event handler that prints out user input on button click"""
        print('greet')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_field(self):
        """An event handler that clears both the text field and output label to blank"""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
