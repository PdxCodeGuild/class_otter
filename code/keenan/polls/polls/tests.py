import datetime
from venv import create
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# this function creates questions for each of our tests
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


# by using the """ """ annotation below we can use that comment as part of the testing output
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published recently() method should return False for questions with a pub_date in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        This method should return False if a question was published over 1 day ago
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        """
        was it published recently
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class IndexViewTests(TestCase):
    
    def test_no_questions(self):
        """
        This method checks if the index page has no questions
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        question = create_question(question_text="Past question.", days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
    
    def test_future_question(self):
        question = create_question(question_text="Future question.", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_future_question_and_past_question(self):
        past_question = create_question(question_text="Past question.", days=-10)
        future_question = create_question(question_text="Future question.", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, past_question.question_text)
        self.assertNotContains(response, future_question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])

    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-10)
        question2 = create_question(question_text="Past question 2.", days=-31)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, question1.question_text)
        self.assertContains(response, question2.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [question1, question2])

class DetailViewTests(TestCase):

    def test_future_question(self):
        future_question = create_question(question_text='Future question.', days=1)
        # this is as a tuple
        response = self.client.get(reverse('polls:detail', args=[future_question.id]))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past Question.', days=-1)
        #this is as a list
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        # assert that the response, contains past_question.question_text
        self.assertContains(response, past_question.question_text)
        # test that the one right thing makes it to our html? if it was multiple things it would be assertQUERYSETEqual
        self.assertEqual(response.context['question'], past_question)