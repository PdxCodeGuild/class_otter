import datetime
# import django

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice


def create_question_with_days(question_text, days):
    # 'timezone' and 'datetime' seem to have same format.
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_question():
    time = timezone.now()
    return Question.objects.create(question_text="Question text", pub_date=time)

def create_choice(question):
    return Choice.objects.create(question=question, choice_text="Choice text")

def print_current_status_of_questions_and_choices():
        print(f"Question.objects.all(): {Question.objects.all()}")
        print(f"len(Question.objects.all()): {len(Question.objects.all())}")
        print(f"Choice.objects.all(): {Choice.objects.all()}")
        print(f"len(Choice.objects.all()): {len(Choice.objects.all())}")


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is the future.
        """
        time_in_future = timezone.now() + datetime.timedelta(hours=1)
        future_question = Question(pub_date=time_in_future)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within last 24 hours.
        """
        time_more_than_twenty_four_hours_ago = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time_more_than_twenty_four_hours_ago)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within last 24 hours.
        """
        time_within_twenty_four_hours_ago = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time_within_twenty_four_hours_ago)
        self.assertIs(recent_question.was_published_recently(), True)
    
    def test_has_two_or_more_choices_with_one_choice(self):
        """
        has_two_or_more_choices() returns False for question which has less than two 'choice's.
        """
        question = create_question()
        create_choice(question)
        # print_current_status_of_questions_and_choices()
        self.assertFalse(question.has_two_or_more_choices())
    
    def test_has_two_or_more_choices_with_two_choices(self):
        """
        has_two_or_more_choices() returns True for question which has two 'choice's.
        """
        question = create_question()
        create_choice(question)
        create_choice(question)
        # print_current_status_of_questions_and_choices()
        self.assertTrue(question.has_two_or_more_choices())
    
    def test_has_two_or_more_choices_with_three_choices(self):
        """
        has_two_or_more_choices() returns True for question which has greater than two 'choice's.
        """
        question = create_question()
        create_choice(question)
        create_choice(question)
        create_choice(question)
        # print_current_status_of_questions_and_choices()
        self.assertTrue(question.has_two_or_more_choices())

    def test_has_only_one_obvious_choice_with_zero_choices(self):
        """
        has_only_one_obvious_answer() returns False if question has zero 'choice's.
        """
        question = create_question()
        # print_current_status_of_questions_and_choices()
        self.assertFalse(question.has_only_one_obvious_choice())

    def test_has_only_one_obvious_choice_with_one_choice(self):
        """
        has_only_one_obvious_answer() returns True if question has exactly one 'choice'.
        """
        question = create_question()
        create_choice(question)
        # print_current_status_of_questions_and_choices()
        self.assertTrue(question.has_only_one_obvious_choice())        

    def test_has_only_one_obvious_choice_with_more_then_one_choice(self):
        """
        has_only_one_obvious_answer() returns False if question has more than one 'choice'.
        """
        question = create_question()
        create_choice(question)
        create_choice(question)
        # print_current_status_of_questions_and_choices()
        self.assertFalse(question.has_only_one_obvious_choice()) 


class IndexViewTests(TestCase):
    
    def test_no_questions(self):
        """
        IndexView() returns 'No polls are available.' with a 200 status when no questions are available.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        """
        IndexView() returns a question which was published in the past.
        """
        question = create_question_with_days(question_text="Past question.", days=-10)
        # print(reverse('polls:index'))  # /polls/
        # print(reverse('polls:detail', args=[question.id]))  # /polls/1/
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
    
    def test_future_question(self):
        """
        IndexView() returns 'No polls are available.' with a 200 status when all pub_date's are in future.
        """
        create_question_with_days(question_text="Future question.", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_future_question_and_past_question(self):
        """
        IndexView() returns only past published questions when both past and future pub_date's are available.
        """
        past_question = create_question_with_days(question_text="Past question.", days=-10)
        future_question = create_question_with_days(question_text="Future question", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, past_question.question_text)
        self.assertNotContains(response, future_question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])
    
    def test_two_past_questions(self):
        """
        IndexView() returns multiple questions which have pub_dates in the past.
        """
        first_past_question = create_question_with_days(question_text="First past question.", days=-10)
        second_past_question = create_question_with_days(question_text="Second past question.", days=-31)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, first_past_question.question_text)
        self.assertContains(response, second_past_question.question_text)
        # Order is important since we have two items in query set.
        self.assertQuerysetEqual(response.context['latest_question_list'], [first_past_question, second_past_question])


class DetailViewTests(TestCase):
    def test_future_question(self):
        """
        DetailView() returns 404 when there are no past pub_date questions.
        """
        future_question = create_question_with_days(question_text="Future question.", days=1)
        # Using list for 'args='
        response = self.client.get(reverse('polls:detail', args=[future_question.id]))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        DetailView() returns a question which has a past pub_date.
        """
        past_question = create_question_with_days(question_text="Past question", days=-1)
        # Using tuple for 'args='
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)
        self.assertEqual(response.context['question'], past_question)


class AddViewTests(TestCase):
    def test_add_question_and_view_on_index_page(self):
        """
        add_question() adds 'question' to database, and 'question' displays on 'index' page.
        """
        # Create dictionary to submit with POST request:
        question_and_choices = {"question": "The question", "choice1": "The first choice", "choice2": "The second choice"}

        # Submit the POST request:
        self.client.post(reverse('polls:add_question'), question_and_choices)
        # GET the resonse:
        index_response = self.client.get(reverse('polls:index'))
        # print(index_response.content)
        # GET response from 'index' should show 'question':
        self.assertContains(index_response, "The question")

    def test_add_question_and_view_on_detail_page(self):
        """
        add_question() adds 'question' and 'choice's to database, and then 'question' and 'choice's display on 'detail' view.
        """
        # Create dictionary to submit with POST request:
        question_and_choices = {"question": "The question", "choice1": "The first choice", "choice2": "The second choice", "choice3": "The third choice"}

        # Submit the POST request:
        self.client.post(reverse('polls:add_question'), question_and_choices)

        # Response from GET request to 'detail' view:
        detail_response = self.client.get(reverse('polls:detail', args=[1]))
        # print(detail_response.content)

        # Response should contain the 'question' and 'choice's:
        self.assertContains(detail_response, "The question")
        self.assertContains(detail_response, "The first choice")
        self.assertContains(detail_response, "The second choice")
        self.assertContains(detail_response, "The third choice")


class DeleteViewTests(TestCase):
    def test_delete_single_question(self):
        """
        delete_single_question() deletes a single 'question' and 'question' no longer shows on 'index' view.

        We are not checking whether the choices are added here. That should be, maybe, done in different test? We are only checking if question is added and deleted. That test was performed with test_add_question_and_view_on_detail_page().
        """
        ## Create a question ##
        # Create dictionary to submit with POST request:
        question_and_choices = {"question": "The question", "choice1": "The first choice", "choice2": "The second choice"}
        # Submit the POST request:
        self.client.post(reverse('polls:add_question'), question_and_choices)

        ## Check question shows on 'index' view ##
        # GET the resonse:
        index_response = self.client.get(reverse('polls:index'))
        # Verify the question is in response:
        self.assertContains(index_response, "The question")
        # Verify, for fun, that a similar question ISN'T in the response:
        self.assertNotContains(index_response, "The question!")

        # How to get the value for the key of the question to be deleted?
        # Not needed. Need to think on this some more.
        # print(index_response.content)      

        ## Delete the question ##
        question_key_dict = {"question_single": 1}
        self.client.post(reverse('polls:delete_single_question'), question_key_dict)

        ## Verify question no longer shows on 'index' view ##
        index_response = self.client.get(reverse('polls:index'))
        # Verify that question ISN'T in the response since it's been deleted:
        self.assertNotContains(index_response, "The question")

    def test_delete_multiple_questions(self):
        """
        delete_multiple_questions() deletes multiple 'question's and 'question's no longer show on 'index' view.

        We are not checking whether the 'choice's are added here. That should be, maybe, done in different test? We are only checking if question is added and deleted.
        """
        ## Create a first question ##
        # Create dictionary to submit with POST request:
        first_question_and_choices = {"question": "The first question", "choice1": "Q1: first choice", "choice2": "Q1: second choice"}
        # Submit the POST request:
        self.client.post(reverse('polls:add_question'), first_question_and_choices)

        ## Create a second question ##
        # Create dictionary to submit with POST request:
        second_question_and_choices = {"question": "The second question", "choice1": "Q2: first choice", "choice2": "Q2: second choice"}
        # Submit the POST request:
        print(f"reverse('polls:add_question'): {reverse('polls:add_question')}")
        self.client.post(reverse('polls:add_question'), second_question_and_choices)

        ## Check questions show on 'index' view ##
        # GET the resonse:
        index_response = self.client.get(reverse('polls:index'))
        # Verify the question is in response:
        self.assertContains(index_response, "The first question")
        self.assertContains(index_response, "The second question")

        ## Delete the question ##
        question_key_dict = {"question_id_1": 1, "question_id_2": 2}
        self.client.post(reverse('polls:delete_multiple_questions'), question_key_dict)

        ## Verify question no longer shows on 'index' view ##
        index_response = self.client.get(reverse('polls:index'))
        # Verify that question ISN'T in the response since it's been deleted:

        self.assertNotContains(index_response, "The first question")
        self.assertNotContains(index_response, "The second question")
