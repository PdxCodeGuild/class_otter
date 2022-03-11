import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

    # Testing Question Model- 3 test cases; 
    # 1 -
    # 2 -
    # 3 - 
class QuestionModelTests(TestCase):
    # case 1 - 
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() method should return False for
        questions with a pub_date in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        # make assertions here
        self.assertIs(future_question.was_published_recently(),False)
# Create your tests here.

        # case 2 - Past (old) Question
    def test_was_published_recently_with_old_question(self):
        """
        old_question_was_published_recently() method should return False for
        questions with a pub_date in the past.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        # make assertions here
        self.assertIs(old_question.was_published_recently(),False)

        # case 3 - Recent        
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() method should return True for
        questions with a pub_date recently.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        recent_question = Question(pub_date=time)
        # make assertions here
        self.assertIs(recent_question.was_published_recently(),True)
        
# Testing Index Views - 5 test cases; 
# 1 - no question found
# 2 - past question found
# 3 - Future Question Found
# 4 - Multiple Questions Found
# 5 - Past and Future Questions Found
        
class IndexViewTests(TestCase):
        # case 1 - No Questions Found
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

       # case 2 - Past Questions Found
    def test_past_questions(self):
        question = create_question(question_text="Past question", days=-10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])
        
        # case 3 - future Questions Found
    def test_future_questions(self):
        create_question(question_text="Future question.", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
 
        # case 4 - multiple Questions Found
    def test_future_question_and_past_question(self):
        past_question= create_question(question_text="Past question.", days=-10)
        future_question = create_question(question_text="future question.", days=10)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, past_question.question_text)
        self.assertNotContains(response, future_question.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])

        # case 5 - two past Questions Found
    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-10)
        question2 = create_question(question_text="Past question 2.", days=-31)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, question1.question_text)
        self.assertContains(response, question2.question_text)
        self.assertQuerysetEqual(response.context['latest_question_list'], [question1, question2])
        
class DetailViewTests(TestCase):
    
        #Case 1 - test for future question
    def test_future_questions(self):
        future_question = create_question(question_text="Future question.", days=1)
        response = self.client.get(reverse('polls:detail', args=[future_question.id]))
        self.assertEqual(response.status_code, 404)

        #case 2 - test for past question
    def test_past_question(self):
       past_question = create_question(question_text="Past question.", days=-1)
       response = self.client.get(reverse('polls:detail', args=[past_question.id],)) # if it doesn't find this - 404
       self.assertContains(response, past_question.question_text)
       self.assertEqual(response.context['question'], past_question) 
        
                   