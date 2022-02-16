from django.db import models

class Question(models.Model):
    # models . ____ fills the database class with fields
    # charfield requires a max length
    # DateTimeField and IntegerField do not require params
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

class Choice(models.Model):
    # SQL databases are considered relational databases, below we are creating a many to one relationship with the Question class above, the first param sets that relationship. 
    # the second parameter defines the related_name to more clearly link them.  the default would be 'choice_set' which is the lowercase name of the class/model
    # the last parameter for on_delete means if the question is deleted, the choices are deleted
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # we include the default as 0 for votes, 
    votes = models.IntegerField(default=0)

# after we updated this we ran the command $python manage.py makemigrations
# this adds a file to the migrations folder

# we create things in this object oriented fashion, to show the things that we need for class types when we utilize this info

# notes from the end of 4/15
# q = Question(question_text="What is your name?", pubdate=timezone.now)
# running this code defines a question what is your name, with the pubdate info now,
# q.save() - this creates the question in the database