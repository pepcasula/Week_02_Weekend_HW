import unittest

from classes.guest import Guest
from classes.song import Song
from classes.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_one = {'name': 'Barney Cannavacciuolo', 'membership': True, 'cash': 32}
        self.guest_two = {'name': 'Nellie Nielsen', 'membership': False, 'cash': 280}
        self.guest_three = {'name': 'Olga Vaan Olafsson', 'membership': True, 'cash': 5}
        self.guest_four = {'name': 'Didier Bundesliga', 'membership': False, 'cash': 19}
        self.guest_five = {'name':'Imma Pyrogy', 'membership': False, 'cash': 130}

    def test_can_add_guest(self):
        newguest = Guest(self.guest_one)
        self.assertEqual('Barney Cannavacciuolo', newguest.check_you_can_add_guest())
    
    def test_check_membership(self):
        membership_check = Guest(self.guest_two)
        self.assertEqual(False, membership_check.check_membership())
    
    def test_guest_can_enter_venue(self):
        can_pay = Guest(self.guest_five)
        self.assertEqual(True, can_pay.check_guest_can_enter_venue())
            
    def test_guest_cannot_enter_venue(self):
        cannot_pay = Guest(self.guest_four)
        self.assertEqual(False, cannot_pay.check_guest_can_enter_venue())