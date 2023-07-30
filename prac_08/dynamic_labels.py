"""
CP1404/CP5632 Practical 8 By Hexon Hartley Jimenez
Dynamic Labels App
Estimated Time: 30 Minutes
Actual Time:  Minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Hexon Hartley Jimenez'


class DynamicNamesApp(App):
    """Main class - Kivy app to demo the dynamic labels program."""

    def build(self):
        """Build the Kivy GUI"""
        Window.size = (750, 450)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root


DynamicNamesApp().run()
