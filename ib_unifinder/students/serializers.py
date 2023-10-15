from rest_framework.serializers import ModelSerializer
from . models import *

class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'