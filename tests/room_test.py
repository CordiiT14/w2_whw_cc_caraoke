from optparse import check_builtin
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

        self.guest_1 = Guest("Ella", 50)
        self.guest_2 = Guest("Adam", 25)
        self.guest_3 = Guest("Laila", 100)
        self.guest_4 = Guest("Robbie", 60)
        self.guest_5 = Guest("Bex", 30)
        self.guest_6 = Guest("Katie", 40)
        self.guest_7 = Guest("Kev", 45)

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
    
    def test_empty_room(self):
        self.room1.check_in_guest_to_room(self.guest_1)
        self.room1.check_in_guest_to_room(self.guest_2)
        self.room1.check_in_guest_to_room(self.guest_3)
        self.room2.check_in_guest_to_room(self.guest_4)
        self.room2.check_in_guest_to_room(self.guest_5)
        self.room1.empty_room()
        self.assertEqual(0, self.room1.number_of_guests_in_room())
        self.assertEqual(2, self.room2.number_of_guests_in_room())

    def test_two_rooms_are_empty(self):
        self.room1.check_in_guest_to_room(self.guest_1)
        self.room1.check_in_guest_to_room(self.guest_2)
        self.room1.check_in_guest_to_room(self.guest_3)
        self.room2.check_in_guest_to_room(self.guest_4)
        self.room2.check_in_guest_to_room(self.guest_5)
        self.room1.empty_room()
        self.room2.empty_room()
        self.assertEqual(0, self.room1.number_of_guests_in_room())
        self.assertEqual(0, self.room2.number_of_guests_in_room())

    def test_add_song_to_room(self):
        song = Song("Enemy", "Imagine Dragons")
        self.room1.add_song(song)
        self.assertEqual(1, len(self.room1.songs))

    def test_add_multiple_songs_to_room(self):
        song_1 = Song("Enemy", "Imagine Dragons")
        song_2 = Song("Lovelost", "Margo")
        self.room1.add_song(song_1)
        self.room1.add_song(song_2)
        self.assertEqual(2, len(self.room1.songs))

        
# Extension 1 - further testing

    def test_room_is_full(self):
        self.room1.guests = [Guest("Ella", 20), Guest("Robbie", 50), Guest("Laila", 30), Guest("Bex", 50), Guest("Katie", 45)]
        self.assertEqual("Sorry, no more space. Pick another room.", self.room1.check_in_guest_to_room(self.guest_7))
    
    