from django.db import models

#This can be done with a single app called grocery_list and model called GroceryItem which contains a text description, a created date, a completed date, and a boolean representing whether it was completed.
# The user should be presented with an input field and a button (in a form). When the clicks the button, it should save the data to the server and show the newly-added item in the list. The user should be presented with a list of incomplete items and a list of complete items. THe user should be able to mark an item complete/incomplete and be able to delete an item.

class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    # completed_date = models.DateTimeField('date completed', blank=True)
    completed_date = models.DateTimeField('date completed', null=True)
    completed = models.BooleanField(default=False)

    def is_completed(self):
        return self.completed


