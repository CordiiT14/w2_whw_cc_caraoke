import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Orange")
        self.room2 = Room("Apple")
        self.room3 = Room("Kiwi")

    def test_room_has_name(self):
        self.assertEqual("Orange", self.room1.room_name)