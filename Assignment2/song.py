#Set the class for managing songs


class Song(object):
    """The song list has title, author, year, and whether it has been studied, set them and add a determination method."""

    def __init__(self, title='', artist='', year=0, is_learned=False):
        self.title = title.title()
        self.artist = artist.title()
        self.year = int(year)
        if is_learned == 'l':
            self.is_learned = True
        elif is_learned == 'u':
            self.is_learned = False
        elif is_learned.__class__ is bool:
            self.is_learned = is_learned
        else:
            raise TypeError()

    # Set the judgment of learned songs
    def song_learned(self):
        self.is_learned = True

    # Set the judgment of unlearned songs
    def song_unlearned(self):
        self.is_learned = False

    def __str__(self):
        status = '(learned)' if self.is_learned else ''
        return f'"{self.title:.35}" by {self.artist:.30} ({self.year!s}) {status}'

    def to_csv_row(self):
        return [
            self.title,
            self.artist,
            str(self.year),
            'l' if self.is_learned else 'u',
        ]
