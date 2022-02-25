from django.test import TestCase

from . import views

class ShortCodeIndexViewTests(TestCase):
    def test_create_short_code_with_eight_characters(self):
        number_of_characters = 8
        short_code = views.create_short_code(number_of_characters)
        self.assertTrue(len(short_code), 8)

    def test_create_short_code_with_default_characters(self):
        short_code = views.create_short_code()
        self.assertTrue(len(short_code), 7)
    
    def test_create_short_code_returns_string(self):
        short_code = views.create_short_code()
        self.assertIsInstance(short_code, str)