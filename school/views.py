
from rest_framework import generics
from .models import Slider , Event,News
from .serializers import SliderSerializer , EventSerializer , NewsSerializer , PartnerLogoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from partnership.models import Partner



# Define the view class
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()  # Retrieve all events from the database
    serializer_class = EventSerializer  # Use the previously defined serializer
    
class NewsByTypeView(APIView):
    def get(self, request):
        news_type = request.query_params.get('news_type', None)
        
        # Filter news by news_type if provided, otherwise return all news
        if news_type:
            news = News.objects.filter(news_type=news_type.upper())
        else:
            news = News.objects.all()
        
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class HomeView(APIView):
    def get(self, request):
        # Fetch the data
        sliders = Slider.objects.all()
        events = Event.objects.all().order_by('-start_date')[:3]  # Last 3 events
        news = News.objects.filter(news_type='INSIDE').order_by('-news_date')[:5]
        headline_news = News.objects.filter(news_type='OUTSIDE').order_by('-news_date')[:5]
        partners = Partner.objects.all()
        # Serialize the data
        slider_serializer = SliderSerializer(sliders, many=True)
        event_serializer = EventSerializer(events, many=True)
        news_serializer = NewsSerializer(news, many=True)
        headline_news = NewsSerializer(headline_news, many=True)
        partners_logo_serializer = PartnerLogoSerializer(partners,many=True)

        # Create the response data
        response_data = {
            "sliders": slider_serializer.data,
            "events": event_serializer.data,
            "news": news_serializer.data,
            "headline_news":headline_news.data,
            "partners_logos" : partners_logo_serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)
    
