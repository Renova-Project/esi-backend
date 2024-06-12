from rest_framework import serializers
from .models import Diplome , Courses

class DiplomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diplome
        fields = '__all__'
        
        
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

