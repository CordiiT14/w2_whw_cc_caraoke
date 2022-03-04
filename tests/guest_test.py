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
