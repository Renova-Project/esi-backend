from rest_framework import serializers
from .models import Oeuvre, StatisticDocument,Directeur,Bibliotheque

class OeuvreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oeuvre
        fields = ['id', 'nom', 'auteur', 'dateAcquisition', 'nombreEmprunt', 'image']

class StatisticDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticDocument
        fields = ['id', 'dateDocumentStatistique', 'lienDocument']

class BibliothequeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliotheque
        fields = '__all__'

class DirecteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directeur
        fields = '__all__'