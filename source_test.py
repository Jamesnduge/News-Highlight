import unittest
from app import models


class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_source = Sources(12,'abcdef','ab@ab.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
