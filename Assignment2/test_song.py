"""(Incomplete) Tests for Song class."""
from song import Song


def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()
    print(default_song)
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned

    # Test initial-value song
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)
    song_2 = Song('Crazy day','Tom Rock',1945,True)
    print(song_2)
    song_4 = Song('Mosdy','Johson Rock',1956,False)
    print(song_4)
run_tests()