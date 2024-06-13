# Create your views here.
from .models import Club, ClubEventExperience
from .serializers import ClubSerializer , EventSerializer , EventExperienceSerializer, ClubDetailSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response 
from school.models import Event
from users.models import UserType
from rest_framework import status
from rest_framework import generics
from users.authentication import IsClub , UserAuthentication
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed


'''
views : 
/- get all clubs                        
- filter club envents   
/- get all events of a club
/- post an event by a club
/- update a post by a club
/- delete a post by a club
/- get all upcoming events of a club

'''



class ClubDetailAPIView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubDetailSerializer
    lookup_field = 'id'
    
    
'''
class UpcomingEventsView(APIView):
    def get(self, request, club_id):
        # Get the current datetime
        current_datetime = datetime.now()
        
        # Query upcoming events for the specific club
        upcoming_events = Event.objects.filter(
            creator=club_id,  # Assuming event_location stores the club identifier
            start_date__gte=current_datetime
        ).order_by('start_date')  # Optional: Order events by start date
        
        # Serialize the queryset
        serializer = EventSerializer(upcoming_events, many=True)
        
        # Return the serialized data as JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)

'''
    
    
class EventCreateView(APIView):
    #authentication_classes = [UserAuthentication]
    #permission_classes = [IsClub] 
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ClubCreateView(generics.CreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubDetailSerializer

    def create(self, request, *args, **kwargs):
        # Set user type to CLUB
        request.data['user']['type'] = UserType.CLUB

        # Validate the incoming data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # If data is valid, proceed with creation
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
class EventUpdateView(APIView):
        
        def put(self, request, id): 
            #test also the user is the owner of the event
            event = Event.objects.get(id=id)
            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     
       


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
    
    

    
    

    
    
    
