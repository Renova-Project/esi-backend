# Create your views here.
from .models import Club
from .serializers import ClubSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 

'''
functions : 
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
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)
    
    

    
    
    
