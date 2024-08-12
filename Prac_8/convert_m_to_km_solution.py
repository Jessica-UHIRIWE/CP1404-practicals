from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

# Conversion constant from miles to kilometers
MILES_TO_KM = 1.60934


class ConvertMilesKmApp(App):
    # Define a property to hold the output kilometers value
    output_km = StringProperty("0.0 km")

    def build(self):
        Window.size = (300, 200)  # Set the window size
        self.title = "Convert Miles to Kilometers"  # Set the window title
        self.root = Builder.load_file('convert_miles_km.kv')  # Load the KV file for the layout
        return self.root

    def handle_convert(self, miles_text):
        """Convert miles to kilometers based on input text."""
        try:
            miles = float(miles_text)  # Convert input text to a float
            kilometers = miles * MILES_TO_KM  # Perform the conversion
            self.output_km = f"{kilometers:.2f} km"  # Update the output string
        except ValueError:
            self.output_km = "0.0 km"  # Default value if conversion fails

    def handle_increment(self, value):
        """Adjust the miles value and update conversion based on increment."""
        try:
            miles = int(self.root.ids.input_miles.text)  # Get current miles value
        except ValueError:
            miles = 0  # Default to 0 if conversion fails

        miles += value  # Adjust the miles value
        self.root.ids.input_miles.text = str(miles)  # Update the input field
        self.handle_convert(str(miles))  # Recalculate the conversion

    def on_text_change(self, miles_text):
        """Update the kilometers output immediately when the text changes."""
        self.handle_convert(miles_text)


ConvertMilesKmApp().run()
