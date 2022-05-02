from django.test import TestCase
from ..models import *

# Create your tests here.

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run Once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_math(self):
        self.assertEqual(2*3, 6)
    

    def test_sp_age(self):
        self.assertEqual(Sportsman.isYoung(25), "Yes")
    
    def test_isMegapolis(self):
        self.assertFalse(City.isMegapolis(400000))
        

    