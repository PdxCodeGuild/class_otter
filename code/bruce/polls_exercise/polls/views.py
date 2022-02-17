from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question, Choice


def index(request):
    # '-pub_date' will order by pub_date descending:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(latest_question_list)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # Old way of getting 'Question':
        # question = Question.objects.get(pk=question_id)
    # A better way, from tutorial:
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    '''Display the 'choice's and votes for a question?'''
    question = Question.objects.get(pk = question_id)
    choices_list = question.choices.all()
    context = {'choices_list': choices_list}
    print(choices_list)
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    '''Allow user to increment the vote number of a choice by one.'''
    question = Question.objects.get(pk = question_id) 
    choices_list = question.choices.all()
    context = {'choices_list': choices_list}
    if request.method == 'GET':
        print("it's a GET!")
        print(request)
        return render(request, 'polls/vote.html', context)

    print("it's a POST!")
    # Do logic to increment vote count:
    return render(request, 'polls/results.html', context)
