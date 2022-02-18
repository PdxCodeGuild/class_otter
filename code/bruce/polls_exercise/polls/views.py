from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

from django.urls import reverse

from django.views import generic

from .models import Question, Choice

# Use generic views:
# https://docs.djangoproject.com/en/4.0/intro/tutorial04/



class IndexView(generic.ListView):
    # Assign some specific variables instead of passing values into 'render()'.
    # Specify the template_name:
    template_name = 'polls/index.html'
    # This is the variable name used in the template html, specified above.
    # 'latest_question_list' used here is important, it has to match the variable in the template html.
    # Specify the context_object_name:
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        # '-pub_date' will order by pub_date descending:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        # 'latest_question_list' above and below can be anything, it's only used inside this class.
        return latest_question_list


# Old detail() view:
    # Old way of getting 'Question':
        # question = Question.objects.get(pk=question_id)
    # A better way, from tutorial:
    # Adds error handling of 404, returns the 'Question', otherwise.
    # question = get_object_or_404(Question, pk=question_id)
    # context = {'question': question}
    # return render(request, 'polls/detail.html', context)

# def detail(request, question_id):
class DetailView(generic.DetailView):
    # We specify 'model' as 'Question', so we don't need to tell Django a 'context' dictionary like we did before. 'Question' class has all the information needed to get stuff from any given 'question'. I'm guessing the 'context_object_name' is automagically 'question' (lower-case of class 'Question').
    model = Question
    # Need to assign the template html to 'template_name'.
    template_name = 'polls/detail.html'


# Similar to detail() view, just need the proper 'template_name':
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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
