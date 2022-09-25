import csv

from song import Song


class SongCollection(object):

    def __init__(self):
        self.songs = []

    def __str__(self):
        _list = '\n'.join(str(song) for song in self.songs)
        return _list
        # return f'<SongCollection [{_list}]>'

    def get_title(self, title):
        for song in self.songs:
            if song.title == title:
                return song
        else:
            return None

    # Open the file load_songs
    def load_songs(self, fp, encoding='ASCII'):
        with open(fp, 'r', encoding=encoding) as f:  # open the csv file
            for row in csv.reader(f):
                print('[Song Info]', row)
                self.songs.append(Song(*row))
                # In the above line of code, row must be in the order of title, artist, year
                # The elements in row must also be no less than 3 or more than 4

    # Save file
    def dump(self, fp, encoding='ASCII'):  # when u quit what will happen
        rows = (song.to_csv_row() for song in self.songs)
        with open(fp, 'w', encoding=encoding, newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)  # write all element into csv file

    # Calculate the numbers of the songs you've learned
    def calc_learned(self):
        # for song in song_list:
        #     if song[3] is True:
        #         self.number_learned += 1
        #     return self.number_learned
        return len([song for song in self.songs if song.is_learned])

    # Calculate the numbers of songs that have not been studied
    def number_of_unlearned(self):
        # for song in song_list:
        #     if song[3] is False:
        #         self.number_unlearned += 1
        #     return self.number_learned
        return len([song for song in self.songs if not song.is_learned])

    # Sort the song list
    def sort(self, keyword: str):
        key = keyword.lower()
        if key in ('artist', 'title', 'year', 'is_learned'):
            self.songs.sort(key=lambda song: getattr(song, key))
        else:
            raise AttributeError(f'Class Song has not attribute "{keyword}"')

    # Add a song
    def add_song(self, song: Song):
        self.songs.append(song)