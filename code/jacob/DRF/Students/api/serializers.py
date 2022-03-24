from dataclasses import fields
from rest_framework import serializers

from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'FirstName', 'LastName', 'Cohort', 'FavoriteTopic', 'FavoriteTeacher', 'Capstone')