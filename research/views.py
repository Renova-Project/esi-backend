from rest_framework import generics
from .models import Teacher
from .serializers import ResearchersSerializer

# Create your views here.


"""
-  les actualites de recherche 
-  nos directeurs de rechereche 
-  les publications de rechereche recents
-  annuaire des chercheurs
-  les repertoires des stages de recherche

-  detail chercheur with {
        cariere 
        equipe 
        publication 
        projet 
        encadrement 
    }
    
"""


class DirectoryOfResearcherView(generics.ListAPIView):
    queryset = Teacher.objects.filter(is_researcher = True)
    serializer_class = ResearchersSerializer
    
class ResearcherDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = ResearchersSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'