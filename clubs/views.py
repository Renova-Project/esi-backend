# Create your views here.
from .models import Club, ClubEventExperience
from .serializers import ClubSerializer , EventSerializer , EventExperienceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 
from school.models import Event
from rest_framework import status

'''
views : 
- get all clubs 
- filter club envents 
- get all events of a club
- post an event by a club
- update a post by a club
- delete a post by a club
- cancel event by a club 
- get all upcoming events of a club

'''



class ClubViewSet(APIView):
    
    def get(request, *args, **kwargs):
        
        # Get all clubs
        clubs = Club.objects.all()
        experiences = ClubEventExperience.objects.all()[:5]
        experiences_serializer = EventExperienceSerializer(experiences, many=True)
                
        events = []
        for club in clubs:
            event = Event.objects.filter(club=club).order_by('-start_date').last()
            event_serializer = EventSerializer(event)
            events.append(event_serializer.data)
            
        clubs_serializer = ClubSerializer(clubs, many=True)
        
        response_data = {
            "clubs": clubs_serializer.data,
            "events": events , 
            "experiences": experiences_serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    

    
    

    
    
    
