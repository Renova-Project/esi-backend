from .models import Club, ClubEventExperience
from school.models import Event
from rest_framework import serializers



class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id','club_name','description']
        
class ClubDetailSerializer(serializers.ModelSerializer): 
    
    class Meta : 
        model = Club
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):  
    class Meta : 
        model = Event
        fields = '__all__'
        
    def validate(self, data):
        
        if not data.get('event_name'):
            raise serializers.ValidationError('Event name is required')
        
        if not data.get('event_description'):
            raise serializers.ValidationError('Event description is required')
        
        if not data.get('event_location'):
            raise serializers.ValidationError('Event location is required')
        
        return data
        
        
        
        
        
        
class EventExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubEventExperience
        fields = ['experience',]