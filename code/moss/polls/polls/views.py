# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

def index(request):
    # return HttpResponse('Hello World!!!')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lates_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f"Your're looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of the question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Your're voting on question {question_id}")
