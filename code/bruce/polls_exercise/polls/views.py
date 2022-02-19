from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone

# Use generic views:
# https://docs.djangoproject.com/en/4.0/intro/tutorial04/


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        # "get_queryset()" is the required function name for Django to know what to do with data result
        # 'latest_question_list' can be any variable, it doesn't seem to be a required naming convention for Django. We use it above since that's what we already have on the template html.
        latest_question_list = Question.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
        return latest_question_list


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        question = Question.objects.filter(pub_date__lte=timezone.now())
        return question


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
