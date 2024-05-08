from rest_framework import viewsets, generics
from .models import Secteur, Organisme, TypeStage, Stage, Candidat, Demande, OffreStage
from .serializers import SecteurSerializer, OrganismeSerializer, TypeStageSerializer, StageSerializer, CandidatSerializer, DemandeSerializer, OffreStageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class SecteurViewSet(viewsets.ModelViewSet):
  queryset = Secteur.objects.all()
  serializer_class = SecteurSerializer


class OrganismeViewSet(viewsets.ModelViewSet):
  queryset = Organisme.objects.all()
  serializer_class = OrganismeSerializer


class TypeStageViewSet(viewsets.ModelViewSet):
  queryset = TypeStage.objects.all()
  serializer_class = TypeStageSerializer


class StageViewSet(viewsets.ModelViewSet):
  queryset = Stage.objects.all()
  serializer_class = StageSerializer

  # Filter stages by sector
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  filter_fields = ['organisme__secteur__nomSecteur']
  search_fields = ['nomStage', 'themeStage', 'descriptionStage', 'organisme__nomOrganisme', 'typestage__nomType']
  ordering_fields = ['nomStage', 'datePublication', 'dureeStage']


class CandidatViewSet(viewsets.ModelViewSet):
  queryset = Candidat.objects.all()
  serializer_class = CandidatSerializer


class DemandeViewSet(viewsets.ModelViewSet):
  queryset = Demande.objects.all()
  serializer_class = DemandeSerializer


class OffreStageViewSet(viewsets.ModelViewSet):
  queryset = OffreStage.objects.all()
  serializer_class = OffreStageSerializer
