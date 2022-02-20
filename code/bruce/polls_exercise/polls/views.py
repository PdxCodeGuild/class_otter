from multiprocessing import context
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


# Is 'ResultsView' a required class name?
# Does 'TheResultsView' work?
class TheResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 'request.POST['choice']' returns the id for the 'choice' which was chosen in the form.
        # type(selected_choice) is <class 'polls.models.Choice'>.
        selected_choice = question.choices.get(pk=request.POST['choice'])
        print(f"request type: {type(request)}")
        print(f"Choice 'id': {request.POST['choice']}")
        print(f"Choice type: {type(selected_choice)}")
        print(f"Choice __str__: {selected_choice}")
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        print(f"Choice votes: {selected_choice.votes}")
        selected_choice.votes += 1
        print(f"Choice votes: {selected_choice.votes}")
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def add_question(request):
    try:
        # print(f"type(request): {type(request)}")
        # print(f"request: {request}")

        question_text = request.POST['question']
        # print(f"question_text: {question_text}")

        q = Question.objects.create(question_text=question_text, pub_date=timezone.now())
        
        choice_keys = [
        'choice1',
        'choice2',
        'choice3',
        'choice4',
        'choice5',
        ]
        
        choices = [request.POST[choice] for choice in choice_keys if request.POST[choice] != '']

        # print(f"len(choices): {len(choices)}")

        for choice in choices:
            # print("Start")
            # print(type(choice))
            # print(choice)
            # print(f"choice.isascii(): {choice.isascii()}")
            # print(f"choice.isalpha(): {choice.isalpha()}")
            # print(f"choice.isalnum(): {choice.isalnum()}")
            # print(f"IsEmptyString: {choice == ''}")
            # print(f"IsNotEmptyString: {choice != ''}")
            # print("Done!")
            Choice.objects.create(question=q, choice_text=choice)
        #####################


        # for choice in choice_keys:
        #     choice = request.POST[choice]
        #     if choice != '':
        #         choices.append(choice)

        # choice1 = request.POST['choice1']
        # print(f"choice1: '{choice1}'")
        # choice2 = request.POST['choice2']
        # print(f"choice2: '{choice2}'")
        # choice3 = request.POST['choice3']
        # print(f"choice3: '{choice3}'")
        # choice4 = request.POST['choice4']
        # print(f"choice4: '{choice4}'")
        # choice5 = request.POST['choice5']
        # print(f"choice5: '{choice5}'")


        # # Create each question using the question 'q':
        # choice1 = request.POST['choice1']
        # print(f"choice1: {choice1}")
        # Choice.objects.create(question=q, choice_text=choice1)
        
        # choice2 = request.POST['choice2']
        # print(f"choice2: {choice2}")
        # Choice.objects.create(question=q, choice_text=choice2)
        
        # choice3 = request.POST['choice3']
        # print(f"choice3: {choice3}")
        # Choice.objects.create(question=q, choice_text=choice3)
        
        # choice4 = request.POST['choice4']
        # print(f"choice4: {choice4}")
        # Choice.objects.create(question=q, choice_text=choice4)
        
        # choice5 = request.POST['choice5']
        # print(f"choice5: {choice5}")
        # Choice.objects.create(question=q, choice_text=choice5)

        # Add a message to say question added.
        # --OR--
        # Route user to 'detail' view.
        # print(q.pk)
        return HttpResponseRedirect(reverse('polls:detail', args=(q.pk,)))
    # No question added.
    except:
        return HttpResponseRedirect(reverse('polls:action'))

def action(request):
    context = {'number_choices': range(5)}
    return render(request, 'polls/action.html', context)
