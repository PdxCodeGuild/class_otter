from django.shortcuts import render
# get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# reverse lookup
from django.urls import reverse



# to start you don't need a context for this section

def index(request):
    return render(request, 'shortened_app/index.html')