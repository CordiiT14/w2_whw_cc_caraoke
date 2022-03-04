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

        self.guest_1 = Guest("Ella")
        self.guest_2 = Guest("Adam")
        self.guest_3 = Guest("Laila")
        self.guest_4 = Guest("Robbie")
        self.guest_5 = Guest("Bex")
        self.guest_6 = Guest("Katie")
        self.guest_7 = Guest("Kev")

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

    def test_check_in_guests_to_room(self):
        self.room1.check_in_guest_to_room(self.guest_1)
        self.assertEqual(1, self.room1.number_of_guests_in_room())

    def test_check_in_multiple_guests_to_room(self):
        self.room1.check_in_guest_to_room(self.guest_1)
        self.room1.check_in_guest_to_room(self.guest_2)
        self.room1.check_in_guest_to_room(self.guest_3)
        self.room1.check_in_guest_to_room(self.guest_4)
        self.assertEqual(4, self.room1.number_of_guests_in_room())

    def test_check_in_multiple_guests_to_different_rooms(self):
        self.room1.check_in_guest_to_room(self.guest_1)
        self.room1.check_in_guest_to_room(self.guest_2)
        self.room2.check_in_guest_to_room(self.guest_3)
        self.room3.check_in_guest_to_room(self.guest_4)
        self.assertEqual(2, self.room1.number_of_guests_in_room())
        self.assertEqual(1, self.room2.number_of_guests_in_room())
        self.assertEqual(1, self.room3.number_of_guests_in_room())

    def test_check_out_guests(self):
        self.room1.check_in_guest_to_room(self.guest_1)
        self.room1.check_out_guests(self.guest_1)
        self.assertEqual(0, self.room1.number_of_guests_in_room())

    def test_check_out_guests_room_not_empty(self):
        self.room1.check_in_guest_to_room(self.guest_1)
        self.room1.check_in_guest_to_room(self.guest_2)
        self.room1.check_out_guests(self.guest_1)
        self.assertEqual(1, self.room1.number_of_guests_in_room())

    def test_check_out_one_guest_from_one_room(self):
        self.room1.check_in_guest_to_room(self.guest_1)
        self.room1.check_in_guest_to_room(self.guest_2)
        self.room1.check_in_guest_to_room(self.guest_3)
        self.room2.check_in_guest_to_room(self.guest_4)
        self.room2.check_in_guest_to_room(self.guest_5)
        self.room1.check_out_guests(self.guest_2)
        self.assertEqual(2, self.room1.number_of_guests_in_room())
        self.assertEqual(2, self.room2.number_of_guests_in_room())
    