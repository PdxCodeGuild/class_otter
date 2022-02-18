import datetime

from django.db import models
from django.utils import timezone


# Question objects have two required arguments.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def was_published_recently(self):
        '''Returns true if question published in last 24 hours.'''
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def  __str__(self):
        '''Returns string representation of Question (i.e. the 'question_text'.'''
        return self.question_text


# Choice has two required arguments: 'choice_text' and 'question'.
class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)

    def  __str__(self):
        return self.choice_text