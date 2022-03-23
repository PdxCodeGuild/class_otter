from rest_framework import serializers
from student import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'first_name',
            'last_name',
            'cohort',
            'favorite_topic',
            'favorite_teacher',
            'capstone',
        )
        model = models.Student