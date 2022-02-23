from django.shortcuts import render, get_list_or_404, reverse

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from .models import GroceryItem

def index(request):
    return HttpResponse('ok')

def additem(request, grocery_item_id):
    grocery_list = GroceryItem.objects.get(pk=grocery_item_id)
    

def create

def completed

def delete