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
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        question = create_question_with_days(question_text="Past question.", days=-10)
        # print(reverse('polls:index'))  # /polls/
        # print(reverse('polls:detail', args=[question.id]))  # /polls/1/
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
    
    def test_future_question(self):
        create_question_with_days(question_text="Future question.", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_future_question_and_past_question(self):
        past_question = create_question_with_days(question_text="Past question.", days=-10)
        future_question = create_question_with_days(question_text="Future question", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, past_question.question_text)
        self.assertNotContains(response, future_question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])
    
    def test_two_past_questions(self):
        first_past_question = create_question_with_days(question_text="First past question.", days=-10)
        second_past_question = create_question_with_days(question_text="Second past question.", days=-31)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, first_past_question.question_text)
        self.assertContains(response, second_past_question.question_text)
        # Order is important since we have two items in query set.
        self.assertQuerysetEqual(response.context['latest_question_list'], [first_past_question, second_past_question])


class DetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question_with_days(question_text="Future question.", days=1)
        # Using list for 'args='
        response = self.client.get(reverse('polls:detail', args=[future_question.id]))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question_with_days(question_text="Past question", days=-1)
        # Using tuple for 'args='
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)
        self.assertEqual(response.context['question'], past_question)

    

