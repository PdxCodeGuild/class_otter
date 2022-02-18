import datetime
from urllib import response
import django

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(question_text, days):
    # 'timezone' and 'datetime' seem to have same format.
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is the future.
        """
        # time_in_future = timezone.now() + datetime.timedelta(days=30)
        time_in_future = timezone.now() + datetime.timedelta(seconds=1)
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


class IndexViewTests(TestCase):
    
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        print(reverse('polls:index'))  # /polls/
        # print(reverse('polls:detail', {'pk': 1}))  #
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
    
    def test_future_question(self):
        create_question(question_text="Future question.", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_future_question_and_past_question(self):
        past_question = create_question(question_text="Past question.", days=-10)
        future_question = create_question(question_text="Future question", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, past_question.question_text)
        self.assertNotContains(response, future_question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])
    
    def test_two_past_questions(self):
        first_past_question = create_question(question_text="First past question.", days=-10)
        second_past_question = create_question(question_text="Second past question.", days=-31)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, first_past_question.question_text)
        self.assertContains(response, second_past_question.question_text)
        # Order is important since we have two items in query set.
        self.assertQuerysetEqual(response.context['latest_question_list'], [first_past_question, second_past_question])


class DetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=1)
        # Using list for 'args='
        response = self.client.get(reverse('polls:detail', args=[future_question.id]))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question", days=-1)
        # Using tuple for 'args='
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)
        self.assertEqual(response.context['question'], past_question)

    

