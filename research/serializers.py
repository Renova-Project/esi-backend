
from rest_framework import serializers
from .models import Teacher


class ResearchersSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)


    class Meta:
        model = Teacher
        fields = [ 'image' ,'first_name', 'last_name', 'email' , 'office' , 'specialty']
        
        
class ResearcherDEtailSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Teacher
        fields = '__all__'
        
        

        
  

    
