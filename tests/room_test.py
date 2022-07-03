import unittest

from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):        
        self.room_one = {
            'room name': 'latino room',
            'capacity': 35,
            'current guests': 19,
            'playlist' : ['Baila por favor']
            }
        self.room_two = {
            'room name': 'rock classics',
            'capacity': 30,
            'current guests': 12,
            'playlist' : ['Welcome to Hell']
            }
        self.room_three = {
            'room name': 'pop music room',
            'capacity': 55,
            'current guests': 34,
            'playlist' : ['Crazy lazy booh', 'La chanson des foules', 'Baila por favor', 'Smell bells']
            }
        self.room_four = {
            'room name':'hip hop room',
            'capacity': 45,
            'current guests': 45,
            'playlist' : ['Too late bro', 'Crazy lazy booh']
            }
        self.room_five = {
            'room name': 'party room',
            'capacity': 25,
            'current guests': 0,
            'playlist' : []
            }
        
    def test_can_add_room(self):
        newroom = Room(self.room_one)
        self.assertEqual('latino room', newroom.check_you_can_add_room())

    def test_customer_can_check_in(self):
        check_in_status = Room(self.room_two)
        self.assertEqual('free to check in', check_in_status.check_in_status())

    def test_customer_cannot_check_in(self):
        check_in_status = Room(self.room_four)
        self.assertEqual('full capacity, sorry!', check_in_status.check_in_status())
    
    def test_add_guest_to_room(self):
        guest_number = Room(self.room_five)
        self.assertEqual(1, guest_number.add_guest_to_room())

    def test_remove_guest_from_room(self):
        guest_number = Room(self.room_one)
        self.assertEqual(18, guest_number.remove_guest_from_room())

    def test_cannot_add_guest_to_full_room(self):
        check_in_status = Room(self.room_four)
        self.assertEqual('full capacity, sorry!', check_in_status.add_guest_to_room())

    def test_add_song_to_room(self):
        song_to_add = 'La chanson des foules'
        target_room = Room(self.room_five)
        self.assertEqual('La chanson des foules', target_room.add_song_to_room(song_to_add))

    def test_remove_song_from_room(self):
        song_to_remove = 'Smell Bells'
        target_room = Room(self.room_two)
        self.assertEqual('Welcome to Hell', target_room.remove_song_from_room(song_to_remove))