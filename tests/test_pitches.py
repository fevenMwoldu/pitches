import unittest
from app.models import Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the pitch model
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(1,'This is for testing a pitch class','20','10')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))