from rest_framework import serializers
from students import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'cohort',
            'favorite_topic',
            'favorite_teacher',
            'capstone'
        )
        model = models.Student