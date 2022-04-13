from rest_framework.serializers import ModelSerializer
from students.models import Students

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
