from django.test import TestCase
from django.urls import reverse

from .models import ShortCode

from . import views

# Helper function to create new ShortCode.
def new_short_code(
    provided_url='https://www.djangoproject.com/', provided_code='1234zyx', provided_description='Django website'
    ):
    return ShortCode.objects.create(
        url=provided_url, code=provided_code, url_description=provided_description
        )


class ShortCodeModelTests(TestCase):

    def test_new_short_code_shows_up_in_database(self):
        """
        Short Code appears in database when created.
        """
        new_short_code()
        db_short_code = ShortCode.objects.get(pk=1)
        self.assertEquals(db_short_code.url, 'https://www.djangoproject.com/')
        self.assertEquals(db_short_code.url_description, 'Django website')
        self.assertEquals(db_short_code.code, '1234zyx')


class CreateShortCodeTests(TestCase):
    def test_create_short_code_with_eight_characters(self):
        number_of_characters = 8
        short_code = views.create_short_code(number_of_characters)
        self.assertEquals(len(short_code), number_of_characters)

    def test_create_short_code_with_default_seven_characters(self):
        default_number_of_characters = 7
        short_code = views.create_short_code()
        self.assertEquals(len(short_code), default_number_of_characters)
    
    def test_create_short_code_returns_string(self):
        short_code = views.create_short_code()
        self.assertIsInstance(short_code, str)

    def test_create_short_code_returns_alphanumeric(self):
        short_code = views.create_short_code()
        self.assertTrue(short_code.isalnum())


class IndexViewTests(TestCase):

    def test_no_short_codes_available(self):
        """
        index() returns 'No shortened urls available' and a 200 status when no short codes are available.
        """
        response = self.client.get(reverse('short:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No shortened urls available")


class AddViewTests(TestCase):

    def test_add_one_shortened_url(self):
        """
        index() returns response which contains one ShortCode object.
        """
        new_short_code()
        response = self.client.get(reverse('short:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEquals(len(response.context['the_url_sets']), 1)
        self.assertContains(response, 'Django website')
        self.assertContains(response, '1234zyx')
        self.assertContains(response, 'https://www.djangoproject.com/')

    def test_add_two_shortened_urls(self):
        """
        index() returns response which contains one ShortCode object.
        """
        new_short_code()
        new_short_code('https://stackoverflow.com/', 'gfedcba', 'Stack Overflow')
        response = self.client.get(reverse('short:index'))
        self.assertEquals(len(response.context['the_url_sets']), 2)
        self.assertContains(response, 'Django website')
        self.assertContains(response, '1234zyx')
        self.assertContains(response, 'https://www.djangoproject.com/')
        self.assertContains(response, 'Stack Overflow')
        self.assertContains(response, 'gfedcba')
        self.assertContains(response, 'https://stackoverflow.com/')


class RedirectToPageViewTests(TestCase):

    def test_redirect_to_page_succeeds_for_existent_code(self):
        """
        redirect_to_page() redirects and returns status_code '302' for existing short code.
        """
        new_short_code()
        response = self.client.get(reverse('short:redirect_to_page', args=['1234zyx']))
        self.assertEquals(response.status_code, 302)

    def test_redirect_to_page_fails_404_for_no_code(self):
        """
        redirect_to_page() fails and returns '404' for non-existent short code.
        """
        new_short_code()
        response = self.client.get(reverse('short:redirect_to_page', args=['1234567']))
        self.assertEquals(response.status_code, 404)


