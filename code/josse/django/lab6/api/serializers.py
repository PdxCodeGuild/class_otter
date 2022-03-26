from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'cohort',
                  'favorite_topic', 'favorite_teacher')
