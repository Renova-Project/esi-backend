from django.http import JsonResponse
from rest_framework import generics
from .models import Diplome , Courses
from .serializers import DiplomeSerializer ,CoursesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 


# Create your views here.
def partners_view(request):
    partners = [
        {'name': 'Partner 1', 'location': 'Location 1'},
        {'name': 'Partner 2', 'location': 'Location 2'},
        {'name': 'Partner 3', 'location': 'Location 3'},
    ]
    
    return JsonResponse({'partners': partners})

class PostDiplome(generics.CreateAPIView):
    queryset = Diplome.objects.all()
    serializer_class = DiplomeSerializer
    
class CoursesView(APIView):
    
    def get(self, request):
        query_set = Courses.objects.all()[:5]
        serilizer  = CoursesSerializer(query_set , many=True)
        return Response(serilizer.data)
    
    
    