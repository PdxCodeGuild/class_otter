from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone

# Use generic views:
# https://docs.djangoproject.com/en/4.0/intro/tutorial04/

max_number_of_questions_to_display = 10


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        # "get_queryset()" is the required function name for Django to know what to do with data result
        # 'latest_question_list' can be any variable, it doesn't seem to be a required naming convention for Django. We use it above since that's what we already have on the template html.
        latest_question_list = Question.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:max_number_of_questions_to_display]
        return latest_question_list


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        question = Question.objects.filter(pub_date__lte=timezone.now())
        return question


# Is 'ResultsView' a required class name?
# Does 'TheResultsView' work? It seems it does work.
class TheResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 'request.POST['choice']' returns the id for the 'choice' which was chosen in the form.
        # type(selected_choice) is <class 'polls.models.Choice'>.
        selected_choice = question.choices.get(pk=request.POST['choice'])
        # print(f"request type: {type(request)}")
        # print(f"Choice 'id': {request.POST['choice']}")
        # print(f"Choice type: {type(selected_choice)}")
        # print(f"Choice __str__: {selected_choice}")
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
    else:
        # print(f"Choice votes: {selected_choice.votes}")
        selected_choice.votes += 1
        # print(f"Choice votes: {selected_choice.votes}")
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

max_number_of_choices_to_add = 5

def add_question(request, max_number_of_choices_to_add=max_number_of_choices_to_add):
    try:
        question_text = request.POST['question']
        # print(f"question_text: {question_text}")


        # choice_text = request.POST['choice2']
        # print(f"choice_text: {choice_text}")

        q = Question.objects.create(question_text=question_text, pub_date=timezone.now())
        # print(f"q: {q}")

        # choice_text = request.POST['choice1']
        # # print(f"choice_text: {choice_text}")
        # c = Choice.objects.create(question=q, choice_text=choice_text)
        # # print(c.choice_text)


        possible_choice_keys = [f"choice{i + 1}" for i in range(max_number_of_choices_to_add)]
        # print(f"possible_choice_keys: {possible_choice_keys}")


        ################### Comment out these two lines to pass the line in tests ###################
        # NOTE: The list comprehension fails when using tests, and the except block is run: 'polls:add'
        # choices = [request.POST[choice] for choice in choice_keys if request.POST[choice] != '']
        # print(f"choices: {choices}")
        ########## self.assertRedirects(post_response, reverse('polls:detail', args=(1,)), status_code=302) <-- Passes! TEST LINE
        #############################################################################################

        # ################### UNCOMMENT out these two lines to pass the line in tests ###################
        # # NOTE: The list comprehension works for adding to db but fails in tests: 'polls:detail'
        # choices = [request.POST[choice] for choice in choice_keys if request.POST[choice] != '']
        # print(f"choices: {choices}")
        # ########## self.assertRedirects(post_response, reverse('polls:add'), status_code=302) <-- Passes! TEST LINE
        # #############################################################################################

        choice_texts = []
        # Try to build choices:
        for key in possible_choice_keys:
            try:
                if request.POST[key] != '':
                    choice_texts.append(request.POST[key])
            except:
                continue
        print(f"choice_texts: {choice_texts}")

        print("Build choices:")
        for choice in choice_texts:
            # print(f"choice: {choice}")
            Choice.objects.create(question=q, choice_text=choice)

        # Question has been added.
        print("Added: True")
        return HttpResponseRedirect(reverse('polls:detail', args=(q.pk,)))

    # No question added.
    except:
        print("Added: False")
        return HttpResponseRedirect(reverse('polls:add'))

def add(request, max_number_of_choices_to_add=max_number_of_choices_to_add):
    """
    Route user to page where they can create a question with up to max_number_of_choices_to_add 'choice's.
    
    Default value is given in function signature.
    """
    context = {'number_choices': range(max_number_of_choices_to_add)}
    return render(request, 'polls/add.html', context)


class DeleteView(generic.ListView):
    template_name = 'polls/delete.html'
    context_object_name = 'question_list'
    def get_queryset(self):
        """
        Return the questions.
        """
        question_list = Question.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:max_number_of_questions_to_delete]
        # question_list = Question.objects.all()
        return question_list


def delete_single_question(request):
    try:
        pk = request.POST['question_single']
        # print(pk)
        question = Question.objects.get(pk=pk)
        print(f"Deleting: {question}")
        # print(Question.objects.all())
        
        # Delete the question.
        result = question.delete()
        print(f"Deleted: {result}")

        # print(Question.objects.all())

        # Question has been deleted.
        return HttpResponseRedirect(reverse('polls:index'))

    # No question deleted.
    except:
        return HttpResponseRedirect(reverse('polls:delete'))

max_number_of_questions_to_delete = max_number_of_questions_to_display

def delete_multiple_questions(request, max_number_of_questions_to_delete=max_number_of_questions_to_delete):
    question_keys = [f"question_id_{i + 1}" for i in range(max_number_of_questions_to_delete)]
    # print(f"question_keys: {question_keys}")

    working_list = []
    # 'try' to delete the questions:
    try:
        # Get list of keys of questions to delete:
        for key in question_keys:
            # 'try' to get the value from request object.
            try:
                working_list.append(request.POST[key])
            # 'except' if item doesn't exist.
            except:
                continue
        
        # For loop to 'try' to delete each question selected:
        for question_id in working_list:
            try:
                # print(Question.objects.get(pk=question_id))
                print(f"To delete: {Question.objects.get(pk=question_id)}")
                print(f"Deleted: {Question.objects.get(pk=question_id).delete()}")
            except:
                continue

        # print(f"working_list to delete: {working_list}")
        # Question has been Deleted.
        print("Deleted: True")
        return HttpResponseRedirect(reverse('polls:index'))

    # No question Deleted.
    except:
        print("Deleted: False")
        return HttpResponseRedirect(reverse('polls:delete'))


