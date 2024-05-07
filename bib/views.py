from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Oeuvre, StatisticDocument
from .serializers import OeuvreSerializer, StatisticDocumentSerializer

class OeuvreListCreate(generics.ListCreateAPIView):
    queryset = Oeuvre.objects.all()
    serializer_class = OeuvreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['auteur']

class OeuvreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oeuvre.objects.all()
    serializer_class = OeuvreSerializer

class StatisticDocumentListCreate(generics.ListCreateAPIView):
    queryset = StatisticDocument.objects.all()
    serializer_class = StatisticDocumentSerializer

class StatisticDocumentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StatisticDocument.objects.all()
    serializer_class = StatisticDocumentSerializer

class SearchView(generics.ListAPIView):
    serializer_class = OeuvreSerializer  # You can change this to the appropriate serializer
    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Oeuvre.objects.filter(nom__icontains=query)  # by the name field
