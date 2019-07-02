import unittest
from app.models import User

class UserTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the pitch model
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(1,'feven','feven@gmail.com','This is my biograph','/home/feven/Pictures/Moringa_pics'.'123abc')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))