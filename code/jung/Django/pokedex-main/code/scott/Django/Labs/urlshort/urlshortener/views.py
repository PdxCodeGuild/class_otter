'''
Shortener views
'''
from django.shortcuts import render, get_object_or_404 # We will use it later
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Urlshort

from .forms import ShortenerForm

def home_view(request):  
    template = 'urlshortener/home.html'
    context = {}
    context['form'] = ShortenerForm() # Empty form
    if request.method == 'GET':  # for HTTP method equals 'GET': passes the Shortener form used to create Shortened objects as the context.
        return render(request, template, context)
    
    elif request.method == 'POST':# for HTTP method equals 'POST': it still passes the form in the context (because the user should be able to enter another URL.
                                  # but this will also pass the 'Post' request to another form called "used_form."
        used_form = ShortenerForm(request.POST)
        test_url = request.POST.get('long_url')
        
        if used_form.is_valid(): # This was a suggested safe way of processing if the user didn't eneter a valid url. It gets the forms errors

            try:
                shortened_object = Urlshort.objects.get(long_url=test_url)
                context['times_followed'] = shortened_object.times_followed

            except:
                shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.short_url # request object method build_absolute_uri gets the 
            long_url = shortened_object.long_url                                   # complete site URL dynamically.
            context['new_url']  = new_url
            context['long_url'] = long_url
            return render(request, template, context)

        context['errors'] = used_form.errors   

        return render(request, template, context)
    
def redirect_url_view(request, shortened_part): # 'try/except' statement to protect the view in the case that the shortened part isn’t 
                                                # found in the db. If the object is found, it increments the times_followed field 
                                                # (for potential Metrics) and then redirects with the HttpResponseRedirect function to 
                                                # the URL that corresponds to the random code.
    
    try:
        shortener = Urlshort.objects.get(short_url=shortened_part)
        shortener.times_followed += 1 #increments the times_followed field if object found       
        shortener.save()
        return HttpResponseRedirect(shortener.long_url) # HttpResponseRedirect function redirects to the URL (long_url) that corresponds to the random code
    except:
        raise Http404('This link appears to be broken') 