import unittest
from app.models import Category

class CategoryTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the pitch model
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_category = Category(1,'feven','Interview')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))