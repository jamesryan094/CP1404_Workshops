from kivy.app import App
from kivy.lang import Builder

class Converter(App):
    def build(self):
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('converter_layout.kv')
        return self.root

    def increment_up(self):
        num = int(self.root.ids.text_input.text) + 1
        self.root.ids.text_input.text = str(num)

    def increment_down(self):
        num = int(self.root.ids.text_input.text) - 1
        self.root.ids.text_input.text = str(num)

    def perform_conversion(self):
        try:
            num = int(self.root.ids.text_input.text)
            self.root.ids.label.text = str(num * 1.61)
        except TypeError:
            self.root.ids.label.text = 'Enter a valid value (any whole number)'




Converter().run()