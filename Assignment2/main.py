"""
Name:Bohan Yu
Date: 19.09.2022 - 25.09.2022
Brief Project Description:This time our project is the creation of a simple interface for a VOD-like application,
with learning songs, arranging songs,adding songs, and displaying the number of songs learned and the number for learning,
as well as a clear button and an error checking procedure.
GitHub URL:https://github.com/JCUS-CP1404/assignment-2---songs-YuBohan-Jcu.git
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from songcollection import SongCollection
from song import Song
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner


# Set up Class


class SongsToLearnApp(App):

    # Get the class we wrote for SongCollection here
    song_list = SongCollection()



    # Main framework structure
    def build(self):
        # To name
        self.title = "Songs to learn --- Yu Bohan"
        # Read kv file
        self.root = Builder.load_file('app.kv')
        # Read csv file
        self.song_list.load_songs("songs.csv")
        # Categories
        self.song_list.sort('Artist')
        # Set button
        self.build_left_widgets()
        self.build_right_widgets()
        return self.root

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_list = SongCollection()  # Get SongCollection
        self.top_label = Label(text="")    # The top broadcast module on the right
        self.sort_label = Label(text="Sort by:") # Left side of the board
        self.spinner = Spinner(text='Artist', values=('Artist', 'Title', 'Year', 'Learned'))  # Set up categories here
        self.append_Songs_label = Label(text="Add Song...") # Left panel
        self.title_label = Label(text="Title:")
        self.title_text_input = TextInput(write_tab=False, multiline=False) # Set title text box
        self.artist_label = Label(text="Artist:")
        self.artist_text_input = TextInput(write_tab=False, multiline=False) # Set the artist text box
        self.year_label = Label(text="Year:")
        self.year_text_input = TextInput(write_tab=False, multiline=False) #Set Year text box
        self.append_Songs_button = Button(text='Add Song') # Add song button on the left
        self.clear_button = Button(text='Clear') # Clear button on the left

    # Set the left button
    def build_left_widgets(self):
        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.append_Songs_label)
        self.root.ids.leftLayout.add_widget(self.title_label)
        self.root.ids.leftLayout.add_widget(self.title_text_input)
        self.root.ids.leftLayout.add_widget(self.artist_label)
        self.root.ids.leftLayout.add_widget(self.artist_text_input)
        self.root.ids.leftLayout.add_widget(self.year_label)
        self.root.ids.leftLayout.add_widget(self.year_text_input)
        self.root.ids.leftLayout.add_widget(self.append_Songs_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.topLayout.add_widget(self.top_label)
        self.spinner.bind(text=self.sorting_songs)
        self.append_Songs_button.bind(on_release=self.append_Songs_handler)
        self.clear_button.bind(on_release=self.fields_text_clearer)


    # (add song)
    def append_Songs_handler(self, *args):
        # If there is a fill-in-the-blank that is vacant.
        if str(self.title_text_input.text).strip() == '' or str(self.artist_text_input.text).strip() == '' or str(
                self.year_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        # If the fill-in blanks are not vacant, then, the following cases
        else:
            # Judgment
            try:
                # If the number is less than 0, then
                if int(self.year_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Year must be >= 0"
                else:
                    # use SongCollection().add_song, Song()
                    self.song_list.add_song(
                        Song(self.title_text_input.text, self.artist_text_input.text,
                             self.year_text_input.text))
                    # Automatic sorting
                    self.sorting_songs(self.spinner.text)
                    self.fields_text_clearer()
                    self.root.ids.rightLayout.clear_widgets()
                    self.build_right_widgets()
            # If there are other inputs that are not numeric.
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    # Set the right label and button
    def build_right_widgets(self):
            # Use the number_of_unlearned and cal_learnt in SongCollection to calculate the unlearned and learned songs
            self.top_label.text = "To Learn: " + str(self.song_list.number_of_unlearned()) + ". Learnt: " + str(
                self.song_list.calc_learned())
            # Turn every song in the csv file into a button
            for song in self.song_list.songs:
                if song.is_learned:
                    text = '"{}" by {}({})(learned)'.format(song.title, song.artist, song.year)
                    song_button = Button(text=text)
                    # Set button color
                    song_button.background_color = [2, 1, 0, 0.3]
                else:
                    text = '"{}" by {}({})'.format(song.title, song.artist, song.year)
                    song_button = Button(text=text)
                    # Set button color
                    song_button.background_color = [0, 88, 88, 0.3]

                song_button.bind(on_release=self.learn_songs)
                self.root.ids.rightLayout.add_widget(song_button)
    # Set the button function for learning songs
    def learn_songs(self, button):
        title = button.text.split("\"")[1]
        first = self.song_list.get_title(title)
        if first is None:
            raise RuntimeError('Not any songs were match this title')
        if first.is_learned:
            self.root.ids.bottomLayout.text = "You have learned " + str(self.song_list.get_title(title).title)
        else:
            self.song_list.get_title(title).song_learned()
            self.root.ids.bottomLayout.text = "You have learned " + str(self.song_list.get_title(title).title)

        self.root.ids.rightLayout.clear_widgets()
        self.build_right_widgets()

    # Clearance
    def fields_text_clearer(self, *args):
        self.root.ids.rightLayout.clear_widgets()

    # Sort Songs
    def sorting_songs(self, *args):
        self.song_list.sort(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.build_right_widgets()

    # Stop
    def on_stop(self):
        self.song_list.dump('./songs_backup.csv')




if __name__ == "__main__":
    SongsToLearnApp().run()