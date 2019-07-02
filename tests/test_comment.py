import unittest
from app.models import Comment

class UserTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the pitch model
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment('This is my comment')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))