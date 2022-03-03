from django.shortcuts import render
# get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# reverse lookup
from django.urls import reverse


# 2 views
# One to submit a url
# And one to redirect the user

# to start you don't need a context for this section

def index(request):
    return render(request, 'shortened_app/index.html')

def create(request):
    return HttpResponse('Create')


# def redirect(request)


# https://www.espn.com/college-football/story/_/id/33392454/grambling-state-head-football-coach-hue-jackson-defends-hiring-offensive-coordinator-art-briles
# https://www.espn.com/soccer/blog-the-toe-poke/story/4605609/how-chelsea-goalkeeper-kepas-penalty-miss-in-carabao-cup-final-played-out-on-social-media



