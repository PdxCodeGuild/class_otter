import random, string

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import ShortCode


default_code_size = 7
# Helper function for creating short code:
def create_short_code(number_of_characters=default_code_size):
    """
    Generate and return an alphanumeric sequence of length NUMBER_OF_CHARACTERS.
    """
    source_of_characters = string.ascii_letters + string.digits
    random.choice(source_of_characters)
    code_sequence_list = [random.choice(source_of_characters) for _ in range(number_of_characters)]
    code_sequence = ''.join(code_sequence_list)
    return code_sequence

def index(request):
    """
    Displays the current shortened URLs and allows user to create a new one.
    """
    the_url_sets = ShortCode.objects.all()
    # # 'the_url_sets' is of type 'QuerySet'.
    # print(the_url_sets)
    # # <QuerySet [<ShortCode: 1234567 : http://brucestull.com/>, <ShortCode: 3LYwt65 : http://google.com/>, <ShortCode: 3hePGlL : http://flynntknapp.com/>, <ShortCode: 7654321 : https://bit.ly/3JMsuHM>]>
    # print(the_url_sets[0].code)
    # # 1234567
    # print(the_url_sets[0].url)
    # # http://brucestull.com/

    context = {
        'the_url_sets': the_url_sets
    }
    return render(request, 'short/index.html', context)

def accept_code_route_to_page(request, code):
    """
    Gets a short code from url and routes user to new page.
    """
    # We are able to get the short 'code' from the url, now we need to process/find the code in the database to get the associated url.
    print(code)
    shortcode_set = get_object_or_404(ShortCode, code=code)
    print(shortcode_set.url)
    print(shortcode_set.code)

    # return render(request, 'short/index.html', context)
    return HttpResponseRedirect(shortcode_set.url)