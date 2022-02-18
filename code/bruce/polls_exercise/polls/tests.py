import datetime
import django

from django.test import TestCase
from django.utils import timezone

from .models import Question

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


