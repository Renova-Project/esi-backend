# Create your views here.
from rest_framework import generics
from .models import Alumni
from .serializers import AlumniSerializer


class AlumniTestimonyView(generics.ListAPIView):
    queryset = Alumni.objects.filter(is_validated=True)  
    serializer_class = AlumniSerializer  
    
class PostTestimonyView(generics.CreateAPIView):
    queryset = Alumni.objects.all()
    serializer_class = AlumniSerializer