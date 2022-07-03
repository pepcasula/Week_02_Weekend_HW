import unittest

from classes.song import Song
from classes.room import Room
from classes.guest import Guest

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_one = {'title': "Baila por favor"}
        self.song_two = {'title': 'La chanson des foules'}
        self.song_three = {'title': 'Smell bells'}
        self.song_four = {'title': 'The rythm of the early afternoon'}
        self.song_five = {'title':'Welcome to hell'}
        self.song_six = {'title':'Too late bro'}
        self.song_seven = {'title':'Crazy lazy booh'} 

    def test_can_add_song(self):
        newsong = Song(self.song_one)
        self.assertEqual('Baila por favor', newsong.check_you_can_add_song())