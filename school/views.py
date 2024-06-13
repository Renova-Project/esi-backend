
from rest_framework import generics
from .models import Slider , Event,News, SuccessStory, SchoolGallery , Analytics
from .serializers import SliderSerializer , EventSerializer , NewsSerializer , PartnerLogoSerializer, SuccessStoriesSerializer, SchoolGallerySerializer
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status
from partnership.models import Partner
from django.db.models import Q



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
        
        #Analytics.increment_visitors()
        #Analytics.increment_current_month_visitors()

        return Response(response_data, status=status.HTTP_200_OK)

class SearchView(APIView):
    def get(self, request):
        query = request.query_params.get('q', None) 
        
        if not query:
            return Response({"error": "Query parameter 'q' is required"}, status=400)
        
        events = Event.objects.filter(
            Q(event_name__icontains=query) |
            Q(event_type__icontains=query) |
            Q(event_description__icontains=query) |
            Q(event_details__icontains=query) |
            Q(event_location__icontains=query)
        )

        news = News.objects.filter(
            Q(news_name__icontains=query) |
            Q(news_type__icontains=query) |
            Q(news_details__icontains=query)
        )
        

        
        event_serializer = EventSerializer(events, many=True)
        news_serializer = NewsSerializer(news, many=True)

        return Response({
            "events": event_serializer.data,
            "news": news_serializer.data , 
        })
        
class SuccessStroriesView(generics.ListAPIView):
    queryset = SuccessStory.objects.filter(is_validated=True)
    serializer_class = SuccessStoriesSerializer

    
class SuccessStoryDetail(APIView):
    def get(self, request, id):
        story = SuccessStory.objects.get(id=id)
        serializer = SuccessStoriesSerializer(story)
        return Response(serializer.data)



class SchoolGalleryView(generics.ListAPIView) : 
    queryset = SchoolGallery.objects.all()   
    serializer_class =SchoolGallerySerializer
    
    
    
