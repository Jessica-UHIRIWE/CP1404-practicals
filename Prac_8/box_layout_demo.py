from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemoApp(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root_widget = Builder.load_file('box_layout.kv')
        return self.root_widget

    def greet_user(self):
        print('greet')
        self.root_widget.ids.output_label.text = f"Hello {self.root_widget.ids.input_name.text}"

    def clear_fields(self):
        self.root_widget.ids.input_name.text = ''
        self.root_widget.ids.output_label.text = 'Enter your name'

BoxLayoutDemoApp().run()
