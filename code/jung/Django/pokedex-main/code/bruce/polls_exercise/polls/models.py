import datetime

from django.db import models
from django.utils import timezone


# Question objects have two required arguments:
# 'question_text' and 'pub_date'.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def  __str__(self):
        '''
        Returns string representation of question (i.e. the 'question_text'.
        '''
        return f"{self.id} : {self.question_text}"

    def was_published_recently(self):
        '''
        Returns True if question published in last 24 hours.
        '''
        now = timezone.now()
        result = now - datetime.timedelta(days=1) <= self.pub_date <= now
        return result

    def has_two_or_more_choices(self):
        '''
        Returns True if question has two or more choices assigned to it.
        '''
        result = len(self.choices.all()) >= 2
        return result

    def has_only_one_obvious_choice(self):
        '''
        Returns True if question has only one choice.

        This is for comedic effect. When a question 'obviously' only has
        one answer.
        '''
        result = len(self.choices.all()) == 1
        return result


# Choice has two required arguments:
# 'question' and 'choice_text'.
# Choice had one optional argument:
# 'votes' has default=0.
class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)

    def  __str__(self):
        return f"{self.id} : {self.choice_text}"