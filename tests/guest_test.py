import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Ella", 50)
        self.guest_2 = Guest("Adam", 25)
        self.guest_3 = Guest("Laila", 100)
        self.guest_4 = Guest("Robbie", 60)
        self.guest_5 = Guest("Bex", 30)
        self.guest_6 = Guest("Katie", 40)
        self.guest_7 = Guest("Kev", 45)

    def test_guest_has_name(self):
        self.assertEqual("Ella", self.guest_1.name)
    
    def test_guest_has_name_2(self):
        self.assertEqual("Adam", self.guest_2.name)

    def test_guest_has_name_3(self):
        self.assertEqual("Laila", self.guest_3.name)
    
    def test_guest_has_name_4(self):
        self.assertEqual("Robbie", self.guest_4.name)