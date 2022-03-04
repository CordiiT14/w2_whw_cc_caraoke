import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Darkside")
        self.song2 = Song("Lovelost")
        self.song3 = Song("Misfit Toys")
        self.song4 = Song("Arcade")
        self.song5 = Song("Lion")