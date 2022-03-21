# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice

#Buisness State of Logic for latest 5 questions rendering them to a template
def index(request): #index.html
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5] 
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]  #variable = ""objects by decending order by date -pub_date tells it descending (newest 5)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # render original request - template -  
   
def detail(request, question_id): #detail.html
    question = get_object_or_404 (
    Question.objects.filter(pub_date__lte=timezone.now()),
    pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
      
def results(request, question_id): #results.html
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id): #voting
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render (request, "polls/detail.html", {
            'question': question,
            'error_message': "Please select a valid choice."
        })
    selected_choice = question.choices.get(pk=request.POST['choice'])
    selected_choice.votes += 1 #increment
    selected_choice.save()
    
    return HttpResponseRedirect (reverse('polls:results', args=(question.id,))) #args needs list or tuple (requires trailing comma) reverse does a reverse lookup




# return HttpResponse("Hello World!") #Create HttpResponse object and return request
# Long way to do above   
# from django.shortcuts import render - Long way
# from django.template import loader  - Long way
    # template= loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list
    # }
    # output = ", ".join([q.question_text for q in latest_question_list])
    # or
    # output = "<h1>Polls</h1><h2>" + "</h2><h2>".join([q.question_text for q in latest_question_list])
    # print(latest_question_list)
    # return HttpResponse(latest_question_list)