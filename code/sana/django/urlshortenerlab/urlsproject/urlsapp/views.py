
from django.shortcuts import render, redirect
import uuid
from .models import Link


# archives = {}

def index(request):
    # return HttpResponse('page')
    return render(request, 'index.html')

# def home(request):
#     return HttpResponse('home')

# def database(inputurl, shorturl):
#     archives.update({ f"{shorturl}":f"{inputurl}"})

def process(request): 
    if request.method == 'POST':
        print("here2")
        input_url = request.POST['name']      
        print(request.POST)
        unique_url = str(uuid.uuid4())[:7]
        new_url = Link(ulink=input_url, slink=unique_url)
        print(new_url)
        new_url.save()
        print("here1")
    return render(request, 'index.html', {'link' : Link.objects.all(), 'go_url' : new_url.slink})

  
# def send(request):

    # if request.method == 'POST':
    #     request_url = request.POST['input']
    #     if request_url in archives:
    #         accepted_url = archives[request_url]
    #         return HttpResponseRedirect(accepted_url)
    #     else:
    #         return redirect('/')

def goto(request, pk):
    go_url = Link.objects.filter(slink=pk)
    print(go_url)
    # go_url = Link.objects.filter(ulink=pk)
    return redirect('http://'+go_url[0].ulink)

# def shorturl(request, pk):
#     go_url = Link.objects.filter(slink=pk)
#     # print(go_url)
#     # go_url = Link.objects.filter(ulink=pk)
#     return go_url
