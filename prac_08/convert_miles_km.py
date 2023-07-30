"""
CP1404/CP5632 Practical 8 By Hexon Hartley Jimenez
Miles to Kilometres Converter
Estimated Time:
Actual Time:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Hexon Hartley Jimenez'

MILES_TO_KM = 1.60934


class DistanceConverterApp(App):
    """ DistanceConverterApp is a program that converts miles to kilometres"""

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (750, 450)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, update):
        """Handles the buttons up and down upon button press"""

    pass

    def handle_calculation(self):
        value = float(self.root.ids.input_distance.text)
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)


DistanceConverterApp().run()
