from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

from django.urls import reverse

from .models import Question, Choice

# Use generic views:
# https://docs.djangoproject.com/en/4.0/intro/tutorial04/


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
    # Adds error handling of 404, returns the 'Question', otherwise.
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)

# def results(request, question_id):
#     '''Display the 'choice's and votes for a question?'''
#     question = Question.objects.get(pk = question_id)
#     choices_list = question.choices.all()
#     context = {'choices_list': choices_list}
#     print(choices_list)
#     return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # This POST['choice'] (relates to 'name="choice"' in 'datail.html') is the value of 'value="{{ choice.id }}"' in 'detail.html'.
        # Using this method to ensure vote is for a 'choice' related to this 'question'.
        selected_choice = question.choices.get(pk=request.POST['choice'])
    # Two things could go wrong, two errors possible.
        # KeyError if 'choice' doesn't exist.
        # Choice.DoesNotExist if the 'choice' id is not one matched to 'question'.
    except (KeyError, Choice.DoesNotExist):
        # Could break multiple error types and respond with different messages.
        # There is nothing important or unique about 'error_message'. This could be used to pass any kind of string through to the 'render'er.
        # Redisplay the question voting form.
        # render() needs three arguments: 'request', 'template_name', and 'context'.
        return render(
            request,
            'polls/detail.html',
            {
            'question': question,
            'error_message': "You didn't select a choice.",
            }
        )
    else:
        selected_choice.votes += 1
        # Need to .save() the selected_choice.
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # args can be list or tuple: '[question.id]' or '(question.id,)'.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
