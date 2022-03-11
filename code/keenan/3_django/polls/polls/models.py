import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    # models . ____ fills the database class with fields
    # charfield requires a max length
    # DateTimeField and IntegerField do not require params
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    # this dunder string will now show the question_text during other operations like Question.objects.all()
    def __str__(self):
        return self.question_text
    
    # this is something we can add to check to see if a response was published in the last 24 hours
    # in time bigger numbers are more recent.
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # SQL databases are considered relational databases, below we are creating a many to one relationship with the Question class above, the first param sets that relationship. 
    # the second parameter defines the related_name to more clearly link them.  the default would be 'choice_set' which is the lowercase name of the class/model
    # the last parameter for on_delete means if the question is deleted, the choices are deleted
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    # we include the default as 0 for votes, 
    votes = models.IntegerField(default=0)

    # this dunder string will now show the choice_text during other operations like Choice.objects.all()
    def __str__(self):
        return self.choice_text

# after we updated this we ran the command $python manage.py makemigrations
# this adds a file to the migrations folder

# we create things in this object oriented fashion, to show the things that we need for class types when we utilize this info

# notes from the end of 4/15
# q = Question(question_text="What is your name?", pubdate=timezone.now)
# running this code defines a question what is your name, with the pubdate info now,
# q.save() - this creates the question in the databaseq