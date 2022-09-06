'''
Prac_07
Student Name: Yu Bohan
Student ID: 14161276
'''


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class MySimpleProgram(App):
    some_text = StringProperty()

    def __init__(self):
        super().__init__()
        self.name_and_id = {"Bohes": "85458", "Lukas": "59647", "Moral": "98894",
                              "Kara": "99999", "Moserlin": "76458"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_label()
        return self.root

    def create_label(self):
        for name,id in self.name_and_id.items():
            temp_label = Label(text=f"{name}'s ID is {id}")
            self.root.ids.entries_box.add_widget(temp_label)




if __name__ == "__main__":
    run_app = MySimpleProgram()
    run_app.run()