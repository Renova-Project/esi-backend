from .models import Club, ClubEventExperience
from school.models import Event
from rest_framework import serializers



class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):  
    class Meta : 
        model = Event
        fields = '__all__'
        
class EventExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubEventExperience
        fields = ['experience',]