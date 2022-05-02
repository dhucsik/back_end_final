from django.test import TestCase
from ..forms import *

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run Once to set up non-modified data for all class methods.")
        pass 
    
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_feedback(self):
        test = {'author' : 'Someone',
                'feedback' : 'That was great!'}
        form = FeedbackCreate(data = test)
        self.assertFalse(form.is_valid())

    def test_user(self):
        test = {
            'username' : 'someone',
            'age' : 18,
            'email' : 'aaa@gmail.com',
            'city' : 'Almaty',
            'university' : 'SDU',
            'maleF' : 'Female',
            'number' : '87088448227',
        }
        form = UserCreate(data = test)
        self.assertTrue(form.is_valid())
