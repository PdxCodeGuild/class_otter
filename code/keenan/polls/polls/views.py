from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    # latest_question_list = Question.objects.all()
    # order_by() by default orders by id
    # -pub_date is in descending order, so newest will be at the top
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")



# this is a long way to do the index page load from the index.html file.. partial notes from class
# from django.template import loader
   
# template = loader.get_template('polls/index.html')
# ontext = {
#     'latest_question_list': latest_question_list
# }
#  return HttpResponse(template.render(context, request))
# # output = ", ".join([q.question_text for q in latest_question_list])