import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("Ella")
        self.guest2 = Guest("Adam")
        self.guest3 = Guest("Laila")
        self.guest4 = Guest("Robbie")
        self.guest5 = Guest("Bex")
        self.guest6 = Guest("Katie")
        self.guest7 = Guest("Kev")

    def test_guest_has_name(self):
        self.assertEqual("Ella", self.guest1.name)
    
    def test_guest_has_name_2(self):
        self.assertEqual("Adam", self.guest2.name)

    def test_guest_has_name_3(self):
        self.assertEqual("Laila", self.guest3.name)
    
    def test_guest_has_name_4(self):
        self.assertEqual("Robbie", self.guest4.name)