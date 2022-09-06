"""
Prac_07
Student Name: Yu Bohan
Student ID: 14161276
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

Convert_Km = 1.60934


class ConvertToMile(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def To_calculate(self, text):
        print("handle calculate")
        miles = self.convert_result(text)
        self.update_result(miles)

    def up_and_down(self, text, change):
        print("handle increment")
        miles = self.convert_result(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        self.output_km = str(miles * Convert_Km)

    @staticmethod
    def convert_result(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


if __name__ == "__main__":
    converting_number = ConvertToMile()
    converting_number.run()