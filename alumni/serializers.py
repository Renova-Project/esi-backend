
from rest_framework import serializers
from .models import Alumni

class AlumniSerializer(serializers.ModelSerializer):
    
    
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)


    class Meta:
        model = Alumni
        fields = ['id' , 'testimony', 'testimony_rating','first_name', 'last_name']