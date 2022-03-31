from rest_framework import serializers

from  students import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id','first_name', 'last_name', 'cohort', 'favorite_topic', 'favorite_teacher', 'capstone',)
        