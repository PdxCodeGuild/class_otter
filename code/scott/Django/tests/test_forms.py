from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.urls import reverse

from urlreduce.forms import ShortenerForm

class ShortenerFormTest(TestCase):

    def test_form_is_valid(self):
        form_data = {'long_url': 'https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing'}
        form = ShortenerForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_is_invalid(self):
        form_data = {'long_url':'yada'}
        form = ShortenerForm(data=form_data)
        self.assertFalse(form.is_valid(), form.errors)