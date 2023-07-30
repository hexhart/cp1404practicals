from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
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
