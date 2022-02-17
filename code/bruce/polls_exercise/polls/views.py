from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader

from .models import Question

def index(request):
    # '-pub_date' will order by pub_date descending:
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(latest_question_list)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

    # return HttpResponse(latest_question_list)
    # output = '<h1>Polls</h1>' + "</h2><h2>".join(q.question_text for q in latest_question_list) + "</h2>"
    # return HttpResponse(output)

    # template = loader.get_template('polls/indes.html')
    # context = {
    #     'latest_question_list': latest_question_list
    # }
    # return HttpResponse(template.render(context, request))

    # return HttpResponse("Welcome to CATS 2000!")

def detail(request, question_id):
    return HttpResponse(f"You're viewing question {question_id}.")

def results(request, question_id):
    return HttpResponse(f"You're viewing results of question {question_id}.")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
