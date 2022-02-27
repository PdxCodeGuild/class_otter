import random, string

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import ShortCode

SOURCE_OF_CHARACTERS = string.ascii_letters + string.digits

default_code_size = 7
# Helper function for creating short code:
def create_short_code(number_of_characters=default_code_size):
    """
    Generate and return an alphanumeric sequence of length
    NUMBER_OF_CHARACTERS.
    """
    # Use list comprehension to generate a list of length 'number_of_characters'
    # of characters 'SOURCE_OF_CHARACTERS'.
    code_sequence_list = (
        [random.choice(SOURCE_OF_CHARACTERS) for _ in range(number_of_characters)]
        )
    # .join() the list 'code_sequence_list' into a string 'code_sequence_string'.
    code_sequence_string = ''.join(code_sequence_list)
    return code_sequence_string

def index(request):
    """
    Displays the current shortened URLs and allows user to create a new one.
    """
    the_url_sets = ShortCode.objects.all().order_by('-created_date')

    context = {
        'the_url_sets': the_url_sets
    }
    return render(request, 'short/index.html', context)

def index_cards(request):
    """
    Displays the current shortened URLs and allows user to create a new one.
    """
    the_url_sets = ShortCode.objects.all().order_by('-created_date')

    context = {
        'the_url_sets': the_url_sets
    }
    return render(request, 'short/index_cards.html', context)

def index_wide(request):
    """
    Displays the current shortened URLs and allows user to create a new one.
    """
    the_url_sets = ShortCode.objects.all().order_by('-created_date')

    context = {
        'the_url_sets': the_url_sets
    }
    # return render(request, 'short/index_with_materialize.html', context)
    return render(request, 'short/index.html', context)

def redirect_to_page(request, code):
    """
    Gets a short code from url and routes user to new page.
    """
    # 'request' type if 'GET'.
    print(code)
    shortcode_set = get_object_or_404(ShortCode, code=code)
    print(shortcode_set.url)
    print(shortcode_set.code)
    # Redirect user to the 'url' paired with the shortened link displayed:
    return HttpResponseRedirect(shortcode_set.url)

def add(request):
    """
    Gets 'url' from user, generates new 'code', adds 'url' and 'code'
    to database, redirects user to index.
    """
    print(request.POST.keys())
    url_to_shorten = request.POST['long-url']
    the_url_description = request.POST['url-description']
    where_we_came_from = request.POST['our-origin']
    print(where_we_came_from)
    # Create a short 'code' to use with above 'url':
    new_short_code = create_short_code()
    # Add the 'url' and 'code' to database:
    ShortCode.objects.create(code=new_short_code, url=url_to_shorten, url_description=the_url_description)
    # NOTE: I successfully added 'url=asdfasdfsf' and 'code=4p8YIaD',
    # without error. The entered 'url' is not valid. It seems that
    # models.URLField(), which is the 'url' field type, only validates
    # when using admin console?
    where_to_return_to = 'short:index'
    where_to_return_to_dict = {
        'index': 'short:index',
        'index_cards': 'short:index_cards',
    }
    return HttpResponseRedirect(reverse(where_to_return_to_dict[where_we_came_from]))
    # return HttpResponseRedirect(reverse('short:index_cards'))

