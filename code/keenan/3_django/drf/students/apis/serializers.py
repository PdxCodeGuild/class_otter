from rest_framework import serializers

from students_app import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            # these fields currently copied from todos, but they are displaying all info...
            # updated it to only have id name and cohort... will this cause probs? 
            'id',
            'first_name',
            'cohort',
        )
        model = models.Student

