from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect

from urlreduce.models import Shortener
# from urlreduce.forms import ShortenerForm

class ShortenerViewTest(SimpleTestCase):

    def test_home_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_home_view_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
    
    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'urlreduce/home.html')

    def test_home_view_contains_correct_html(self):
        response = self.client.get('')
        self.assertContains(response, '<h1>URL Shortener App <i class="fas fa-link px-2"></i></h1>')
    
    def test_home_view_does_not_contain_correct_html(self):
        response = self.client.get('')
        self.assertNotContains(response, '<p>Holla</p>')

class ShortenerRedirectViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
         Shortener.objects.create(long_url = "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing")

    def test_redirect_url_view_returns_long_url(self):
        shortener = Shortener.objects.get(id=1)
        shortener.save()
        short, long = shortener.short_url, shortener.long_url
        response = self.client.get('/' + short)
        self.assertRedirects(
            response, long, status_code=302,target_status_code=200, fetch_redirect_response=False
        )