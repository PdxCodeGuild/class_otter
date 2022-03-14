from django.test import TestCase

from urlreduce.models import Shortener

class ShortenerModelTest(TestCase):

    @classmethod
    def  setUpTestData(cls):
         Shortener.objects.create(long_url = "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing")
    
    def test_long_url_label(self):
        shortener = Shortener.objects.get(id=1)
        field_label = shortener._meta.get_field('long_url').verbose_name
        self.assertEqual(field_label, 'long url')

    def test_times_followed_label(self):
        shortener = Shortener.objects.get(id=1)
        field_label = shortener._meta.get_field('times_followed').verbose_name
        self.assertEqual(field_label, 'times followed')
    
    def test_created_label(self):
        shortener = Shortener.objects.get(id=1)
        field_label = shortener._meta.get_field('created').verbose_name
        self.assertEqual(field_label, 'created')
    
    def test_short_url_label(self):
        shortener = Shortener.objects.get(id=1)
        field_label = shortener._meta.get_field('short_url').verbose_name
        self.assertEqual(field_label, 'short url')

    def test_short_url_max_length(self):
        shortener = Shortener.objects.get(id=1)
        max_length = shortener._meta.get_field('short_url').max_length
        self.assertEqual(max_length, 15)
    
    def test_object_string_is_long_url_shortened_to_short_url(self):
        shortener = Shortener.objects.get(id=1)
        expected_object_string = f'{shortener.long_url} shortened to {shortener.short_url}'
        self.assertEqual(str(shortener), expected_object_string)