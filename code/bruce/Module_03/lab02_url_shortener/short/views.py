import random, string

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

from .models import ShortCode

from . import utils

DO_PRINT_STUFF_TO_CONSOLE = True
DO_PRINT_STUFF_TO_CONSOLE = False


# TODO: Learn a better way to choose rendered "template" than routing to two separate templates.
# TODO: Learn how to pass the 'pk' from 'add()' view to the appropriate 'index' view. Might need to pass it through the url. Would need to add <int:pk> to path(). Can then pass the 'pk' through the 'context' to render the appropriate "users' recent add" block.
def index(request):
    """
    Renders template 'index.html' to display the current shortened URLs and allows user to create a new one.
    """
    utils.print_meta_data_to_console_return_meta_data_dictionary(request, DO_PRINT_STUFF_TO_CONSOLE)
    
    the_url_sets = ShortCode.objects.all().order_by('-created_date')
    context = {
        'the_url_sets': the_url_sets
    }
    return render(request, 'short/index.html', context)


def index_cards(request):
    """
    Renders template 'index_cards.html' to display the current shortened URLs and allows user to create a new one.
    """
    utils.print_meta_data_to_console_return_meta_data_dictionary(request, DO_PRINT_STUFF_TO_CONSOLE)
    
    the_url_sets = ShortCode.objects.all().order_by('-created_date')
    context = {
        'the_url_sets': the_url_sets
    }
    return render(request, 'short/index_cards.html', context)


def redirect_to_page(request, code):
    """
    Gets a short code from url, usually a link in the app main page, and routes user to destination page.
    """
    utils.print_meta_data_to_console_return_meta_data_dictionary(request, DO_PRINT_STUFF_TO_CONSOLE)
    
    shortcode_set = get_object_or_404(ShortCode, code=code)
    # When we use link for first time we get '301' then '302's afterward. After clearing browser cache, the first redirect is again '301' then '302's afterward.
    # Redirect 'status_code's:
        # 301 : permenent
        # 302 : temporary
    return HttpResponseRedirect(shortcode_set.url)


def add(request):
    """
    Gets 'url' from user, generates new 'code', adds 'url' and 'code'
    to database, redirects user to index view.
    """
    utils.print_post_data_to_console_return_post_data_dictionary(request, DO_PRINT_STUFF_TO_CONSOLE)
    utils.print_meta_data_to_console_return_meta_data_dictionary(request, DO_PRINT_STUFF_TO_CONSOLE)
    
    url_to_shorten = request.POST['long-url']
    the_url_description = request.POST['url-description']
    # 'our-origin' is either 'index' or 'index_cards'.
    where_we_came_from = request.POST['our-origin']
    new_short_code = utils.create_short_code()

    sc = ShortCode.objects.create(code=new_short_code, url=url_to_shorten, url_description=the_url_description)

    # TODO: We can get the 'pk' from the created ShortCode, this will be used to display a block which displays the user's created ShortCode information in redirected view.
    new_code_pk = sc.pk
    print(f"new_code_pk: {new_code_pk}")

    where_to_return_to_dict = {
        'index': 'short:index',
        'index_cards': 'short:index_cards',
    }
    return HttpResponseRedirect(reverse(where_to_return_to_dict[where_we_came_from]))

