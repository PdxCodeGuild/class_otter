from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone

# Use generic views:
# https://docs.djangoproject.com/en/4.0/intro/tutorial04/


# TODO: How to pass max_number_of_questions_to_display into view classes?
# class IndexView(generic.ListView, max_number_of_questions_to_display=max_number_of_questions_to_display):
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        """Return the last five published questions."""
        max_number_of_questions_to_display = 10
        # "get_queryset()" is the required function name for Django to
        # know what to do with data result.
        # 'latest_question_list' can be any variable, it doesn't seem to
        # be a required naming convention for Django. We use it above since
        # that's what we already have on the template html.
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


# Is 'ResultsView' a required class name? This is standard practice but not required.
# Does 'TheResultsView' work? It seems it does work.
class TheResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 'request.POST['choice']' returns the id for the 'choice' which
        # was chosen in the form.
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
        q = Question.objects.create(question_text=question_text, pub_date=timezone.now())
        
        # TODO: I am hard-coding these here. How to automagically produce them?
        # Possible resource: https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#cycle
        possible_choice_keys = [f"choice{i + 1}" for i in range(max_number_of_choices_to_add)]


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
        # print(f"choice_texts: {choice_texts}")

        # print("Build choices:")
        for choice in choice_texts:
            Choice.objects.create(question=q, choice_text=choice)

        # Question has been added.
        # print("Added: True")
        return HttpResponseRedirect(reverse('polls:detail', args=(q.pk,)))

    # TODO: Understand above need to automagically create keys, 'possible_choice_keys'.
    # Client, due to 'required' HTML attribute, verifies that some data has been input.
    # The 'try'/'except'/'continue' allows a question to be created even if choices keys are not proper?
    # So, this redirect to 'polls:add' is never reached?
    # No question added.
    except:
        # print("Added: False")
        return HttpResponseRedirect(reverse('polls:add'))

def add(request, max_number_of_choices_to_add=max_number_of_choices_to_add):
    """
    Route user to page where they can create a question with up to
    max_number_of_choices_to_add 'choice's.
    
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
        return question_list

# TODO: There is a bug where clicking the 'Submit' for 'Delete single question',
# when no radio buttons are selected, and view stays on same page 'delete' view.
# Cliking the 'Submit' for 'Delete multiple questions', when no checkboxes are
# selected, results in view loading for 'index'.
def delete_single_question(request):
    """
    Delete a single 'question'.
    """
    try:
        # Get the primary key from the POST request variable 'question_single':
        pk = request.POST['question_single']
        # Get the question for the primary key received from POST request:
        question = Question.objects.get(pk=pk)
        # print(f"Deleting: {question}")
        
        question.delete()
        # Delete the question and save returned value to display below:
        # result = question.delete()
        # print(f"Deleted: {result}")

        # Question has been deleted.
        # print("Question deleted.")
        return HttpResponseRedirect(reverse('polls:index'))

    # No question deleted.
    except:
        # print("No question deleted.")
        return HttpResponseRedirect(reverse('polls:delete'))

# max_number_of_questions_to_delete = max_number_of_questions_to_display
max_number_of_questions_to_delete = 10

def delete_multiple_questions(request, max_number_of_questions_to_delete=max_number_of_questions_to_delete):
    """
    Delete multiple 'question's.
    """
    # TODO: Figure out how to automagically produce 'question_keys'.
    # Resource: https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#cycle
    # Generate keys in a view then 'cycle' through those same keys in template?
    question_keys = [f"question_id_{i + 1}" for i in range(max_number_of_questions_to_delete)]

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
        
        # print(f"working_list: {working_list}")

        # For loop to 'try' to delete each question selected:
        for question_id in working_list:
            try:
                Question.objects.get(pk=question_id)
                # to_delete = Question.objects.get(pk=question_id)
                # print(f"To delete {question_id}: {to_delete}")
                Question.objects.get(pk=question_id).delete()
                # deleted = Question.objects.get(pk=question_id).delete()
                # print(f"Deleted {question_id}: {deleted}")
            except:
                continue

        # print(f"working_list to delete: {working_list}")
        # Question has been Deleted.
        # print("Deleted: True")
        return HttpResponseRedirect(reverse('polls:index'))

    # No question Deleted.
    except:
        # print("Deleted: False")
        return HttpResponseRedirect(reverse('polls:delete'))


