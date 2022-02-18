# from django.shortcuts import render - Long way
# from django.template import loader  - Long way
# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

from .models import Question

#Buisness State of Logic for latest 5 questions rendering them to a template
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #create a custom. -pub_date tells it descending (newest 5)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # render original request - template -  
   
def detail(request, question_id):
    return HttpResponse(f"you're looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"you are looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse("you are voting on question {question_id}") 

# return HttpResponse("Hello World!") #Create HttpResponse object and return request

# Long way to do above   
    # template= loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list
    # }
    # output = ", ".join([q.question_text for q in latest_question_list])
    # or
    # output = "<h1>Polls</h1><h2>" + "</h2><h2>".join([q.question_text for q in latest_question_list])
    # print(latest_question_list)
    # return HttpResponse(latest_question_list)