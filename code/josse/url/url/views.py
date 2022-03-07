from django.shortcuts import render, get_object_or_404

from url.models import UrlShortner
from django.http import HttpResponseRedirect 
from django.urls import reverse

import string
from random import choice

def code_generator():
    characters = string.ascii_letters + string.digits
    code = "".join(choice(characters) for x in range(7))
    return code

def index(request):
    url_input = UrlShortner.objects.all()
    # print(f"this is all of the UrlShortner objects {url_input}")
    # print(f"this is first {url_input[0]}")
    # print(f"this is database {type(url_input)}")
    # print(f"this is how many obejects {len(url_input)}")
    context = {'url_input' : url_input}
    if request.method == 'POST':
        biggest_url = request.POST['user_submitted_url']
        # print(f" this is going to database {request.POST}")
        # biggest_url = request.POST['long_url']
        # print(request.POST['user_submitted_url'])
        UrlShortner.objects.create(long_url=request.POST['user_submitted_url'],short_url=code_generator())
        return HttpResponseRedirect(reverse('url:index'))
        # return render(request, 'url/index.html',context)
    return render(request, 'url/index.html',context)


def redirect_to_page(request, code):
    """
    redirects short_url to long url.
    """
    # 'request' type if 'GET'.
    # print(code)
    url_class = get_object_or_404(UrlShortner, short_url=code)
    # print(url_class.long_url)
    # print(url_class.short_url)
    # Redirect user to the 'url' paired with the shortened link displayed:
    return HttpResponseRedirect(url_class.long_url)


