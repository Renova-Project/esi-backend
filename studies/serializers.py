from rest_framework import serializers
from .models import Module, Chapitre, Specialite, AnneeEtude, SousObjectif, Bibliographie, Competances, FamilleCompetence, ElementCompetences, Prerequis

class SousObjectifSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousObjectif
        fields = ['id', 'text']

class BibliographieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliographie
        fields = ['id', 'textreference']

class CompetancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competances
        fields = ['id', 'familleCompetence', 'nomCompetence', 'designationCompetence']

class FamilleCompetenceSerializer(serializers.ModelSerializer):
    competences = CompetancesSerializer(many=True, read_only=True)

    class Meta:
        model = FamilleCompetence
        fields = ['id', 'codeFamille', 'designation', 'competences']

class ElementCompetencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementCompetences
        fields = ['id', 'codeElmcompetence', 'designation', 'Niveau']

class PrerequisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerequis
        fields = ['id', 'Text']

class ChapitreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapitre
        fields = ['id', 'num', 'chapitre', 'chapitre_name', 'chapitre_description']

class SpecialiteSerializer(serializers.ModelSerializer):
    modulesS1 = serializers.StringRelatedField(many=True)
    modulesS2 = serializers.StringRelatedField(many=True)
    skills = CompetancesSerializer(many=True, read_only=True)

    class Meta:
        model = Specialite
        fields = ['id', 'nomspecialite', 'designation', 'idSpecialite', 'LifeAs', 'Image', 'videoLink', 'modulesS1', 'modulesS2', 'skills', 'jobslist', 'pdfFile']

class AnneeEtudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnneeEtude
        fields = ['id', 'codeAnnée', 'designation', 'description']

class ModuleSerializer(serializers.ModelSerializer):
    sousobjectifs = SousObjectifSerializer(many=True, read_only=True)
    chapitres = ChapitreSerializer(many=True, read_only=True)
    referencebibliographique = BibliographieSerializer(many=True, read_only=True)
    specialites_s1 = SpecialiteSerializer(many=True, source='specialite_s1')
    specialites_s2 = SpecialiteSerializer(many=True, source='specialite_s2')

    class Meta:
        model = Module
        fields = ['id', 'module_name', 'designation', 'coef', 'volume_cours', 'volume_td', 'objectif', 'sousobjectifs', 'chapitres', 'referencebibliographique', 'specialites_s1', 'specialites_s2']
