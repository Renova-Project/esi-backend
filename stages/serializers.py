from rest_framework import serializers
from .models import Secteur, Organisme, TypeStage, Stage, Candidat, Demande, OffreStage

class SecteurSerializer(serializers.ModelSerializer):
  class Meta:
    model = Secteur
    fields = '__all__'

class OrganismeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Organisme
    fields = '__all__'

class TypeStageSerializer(serializers.ModelSerializer):
  class Meta:
    model = TypeStage
    fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
  typestage = TypeStageSerializer(many=True)  # Nested serializer for many-to-many relationship

  class Meta:
    model = Stage
    fields = '__all__'

class CandidatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Candidat
    fields = '__all__'

class DemandeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Demande
    fields = '__all__'

class OffreStageSerializer(serializers.ModelSerializer):
  # Optionally, include nested serializer for Organisme if needed
  # organisme = OrganismeSerializer()

  class Meta:
    model = OffreStage
    fields = '__all__'
