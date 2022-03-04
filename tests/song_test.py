import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Darkside", "Neoni")
        self.song2 = Song("Lovelost", "Margo")
        self.song3 = Song("Misfit Toys", "Pusha T")
        self.song4 = Song("Arcade", "Duncan Laurence")
        self.song5 = Song("Lion", "Saint Mesa")

    def test_song_has_name(self):
        self.assertEqual("Misfit Toys", self.song3.title)
    
    def test_song_has_name_2(self):
        self.assertEqual("Arcade", self.song4.title)

    def test_song_has_name_4(self):
        self.assertEqual("Lion", self.song5.title)

    def test_song_has_artist(self):
        self.assertEqual("Neoni", self.song1.artist)
    
    def test_song_has_artist_2(self):
        self.assertEqual("Margo", self.song2.artist)

    def test_song_has__artist_3(self):
        self.assertEqual("Saint Mesa", self.song5.artist)