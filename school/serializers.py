# serializers.py
from rest_framework import serializers
from .models import Slider , Event,News
from partnership.models import Partner


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'slider_image', 'slider_description', 'slider_action_name', 'slider_link')
        
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id' , 'event_name', 'start_date', 'end_date']
        

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'news_name', 'news_type', 'news_details', 'news_date', 'image']
        
        
class PartnerLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['organizationId', 'organizationLogo']  # Only return the logo