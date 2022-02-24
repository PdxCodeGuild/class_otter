from django.http import HttpResponse, HttpResponseRedirect
# this get_object_or_404 adds a function that does the same
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice


def index(request):
    # latest_question_list = Question.objects.all()
    # order_by() by default orders by id
    # -pub_date is in descending order, so newest will be at the top
    # pub_date__lte
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # the goo4 function takes 2 arguments, 
    question = get_object_or_404(
        Question.objects.filter(pub_date__lte=timezone.now()),
        pk=question_id
    )
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(
        Question.objects.filter(pub_date__lte=timezone.now()),
        pk=question_id
    )
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist): 
        # 3 args, request, template, context
        return render(request, "polls/detail.html", {
            'question': question, 
            'error_message': "Please select a valid choice."
        })
    selected_choice.votes +=1
    selected_choice.save()
    # reverse expects two parameters, the url we want to redirect to, and which results page in the form of a list or tuple (question.id will error out), doing it with a trailing comma (question.,) tells django that it is a tuple,
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# this is a long way to do the index page load from the index.html file.. partial notes from class
# from django.template import loader
   
# template = loader.get_template('polls/index.html')
# ontext = {
#     'latest_question_list': latest_question_list
# }
#  return HttpResponse(template.render(context, request))
# # output = ", ".join([q.question_text for q in latest_question_list])