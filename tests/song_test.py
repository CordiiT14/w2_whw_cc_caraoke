import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Darkside", "Neoni")
        self.song2 = Song("Lovelost", "Margo")
        self.song3 = Song("Misfit Toys", "Pusha T")
        self.song4 = Song("Arcade", "Duncan Laurence")
        self.song5 = Song("Lion", "Saint Mesa")