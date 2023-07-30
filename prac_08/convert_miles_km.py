"""
CP1404/CP5632 Practical 8 By Hexon Hartley Jimenez
Miles to Kilometres Converter
Estimated Time:
Actual Time:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.properties import StringProperty

__author__ = 'Hexon Hartley Jimenez'

MILES_TO_KM = 1.60934


class DistanceConverterApp(App):
    """
    DistanceConverterApp is a program that converts miles to kilometres
    """
    # output_value = StringProperty()

    def build(self):
        """
        Build the Kivy app from the kv file
        """
        Window.size = (750, 450)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, update):
        """
        Handles the buttons up and down upon button press
        """
        # self.output_value = self.root.ids.input_distance.text
        pass

    def handle_calculation(self):
        """
        Handles the conversion of miles to kilometres
        """
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def get_valid_miles(self):
        """
        Input validation to get the input from the text field, convert it to float.
        """
        try:
            value = float(self.root.ids.input_distance.text)
            return value
        except ValueError:
            return 0


DistanceConverterApp().run()
