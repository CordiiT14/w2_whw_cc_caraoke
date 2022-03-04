import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest
from tests.guest_test import TestGuest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Orange")
        self.room2 = Room("Apple")
        self.room3 = Room("Kiwi")

    def test_room_has_name(self):
        self.assertEqual("Orange", self.room1.room_name)

    def test_second_room_has_name(self):
        self.assertEqual("Apple", self.room2.room_name)

    def test_room_has_empty_guest_list(self):
        self.assertEqual(0, len(self.room3.guests))

    def test_room_has_empty_song_list(self):
        self.assertEqual(0, len(self.room2.songs))
    
    def test_number_of_guests_in_room(self):
        self.assertEqual(0, self.room1.number_of_guests_in_room())

    # def test_check_in_guests_to_room(self):
    #     check_in_guest_to_room(self.room1, TestGuest.guest1)
    #     self.assertEqual(1, len(self.room1))