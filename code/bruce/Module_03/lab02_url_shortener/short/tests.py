from django.test import TestCase
from django.urls import reverse

from .models import ShortCode

from . import utils

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


class ShortCodesUtilsTests(TestCase):

    def test_create_short_code_with_eight_characters(self):
        """
        create_short_code() creates short code of specified length 'number_of_characters = 8'.
        """
        number_of_characters = 8
        short_code = utils.create_short_code(number_of_characters)
        self.assertEquals(len(short_code), number_of_characters)

    def test_create_short_code_with_default_seven_characters(self):
        """
        create_short_code() creates short code of default length '7'.
        """
        default_number_of_characters = 7
        short_code = utils.create_short_code()
        self.assertEquals(len(short_code), default_number_of_characters)
    
    def test_create_short_code_returns_string(self):
        """
        create_short_code() returns a string.
        """
        short_code = utils.create_short_code()
        self.assertIsInstance(short_code, str)

    def test_create_short_code_returns_alphanumeric(self):
        """
        create_short_code() returns an 'alphanumeric' string.
        """
        short_code = utils.create_short_code()
        self.assertTrue(short_code.isalnum())


class IndexViewTests(TestCase):

    def test_no_short_codes_available(self):
        """
        index() response contains 'No shortened urls available' and a 200 status when no short codes are available.
        """
        response = self.client.get(reverse('short:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No shortened urls available")

    def test_one_shortened_url_available(self):
        """
        index() response contains the the attributes of 'one' ShortCode
        object when there is 'one' in the database.
        """
        new_short_code()
        response = self.client.get(reverse('short:index'))
        self.assertEquals(len(response.context['the_url_sets']), 1)
        self.assertContains(response, 'Django website')
        self.assertContains(response, '1234zyx')
        self.assertContains(response, 'https://www.djangoproject.com/')

    def test_two_shortened_urls_available(self):
        """
        index() response contains the attributes of 'two' ShortCode
        objects when 'two' are in the database.
        """
        new_short_code()
        new_short_code('https://stackoverflow.com/', 'gfedcba', 'Stack Overflow')
        response = self.client.get(reverse('short:index'))
        # response 'context' contains 'two' 'ShortCode' objects' attributes in 'the_url_sets'.
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
        redirect_to_page() redirects to 'shortcode_set.url' and 'response' 'status_code' is '302' for existent short code.
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


# class AddViewTests(TestCase):

#     def test_add_view_function(self):
#         """
#         add() gets 'url' and 'url_description' from user, generates 'code', adds 'url_description', 'url' and 'code' to database, sends user back to the same template they sent request from.
#         """
#         new_attributes_and_our_origin_to_send = {
#             'url-description': "Test long URL description",
#             'long-url': "subdomain.domain",
#             'our-origin': "index_cards",
#         }
#         # NOTE: Need to specify 'post()' function here. 'get()' will fail. Since we are not actually using a 'form' 'button', which would have the 'POST' method specified in the tag, we need to use the proper client function 'post()'.
#         # self.client.get(reverse('short:add'), new_attributes_and_our_origin_to_send) # Fails on "KeyError: 'long-url'"
#         self.client.post(reverse('short:add'), new_attributes_and_our_origin_to_send)