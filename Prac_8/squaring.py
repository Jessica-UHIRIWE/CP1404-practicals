"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Jessica UHIRIWE, JCU Brisbane
Started 12/08/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Jessica UHIRIWE'

class SquareNumberApp(App):
    """ A Kivy application for squaring a number """

    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (400, 200)  # Adjusted size for better layout visibility
        self.title = "Square Number"  # Set the window title
        self.root = Builder.load_file('squaring.kv')  # Load the KV file
        return self.root

    def handle_calculate(self, value):
        """ Calculate the square of the input value and update the label """
        try:
            # Convert input value to float and compute its square
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)  # Display the result
        except ValueError:
            # Handle cases where input is not a valid number
            self.root.ids.output_label.text = 'Invalid input'  # Display an error message

if __name__ == "__main__":
    SquareNumberApp().run()  # Run the app
