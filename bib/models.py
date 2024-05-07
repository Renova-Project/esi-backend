# models.py

from django.db import models

class Bibliotheque(models.Model):
    idbib = models.AutoField(primary_key=True)
    nombreMemoire = models.IntegerField()
    nombreThese = models.IntegerField()
    nombreLivre = models.IntegerField()
    horaire = models.CharField(max_length=100)
    documentReglementationInterieur = models.FileField(upload_to='documents/')

class Directeur(models.Model):
    bibliotheque = models.OneToOneField(Bibliotheque, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

class Oeuvre(models.Model):
    bibliotheque = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE)
    idOeuvre = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    dateAcquisition = models.DateField()
    nombreEmprunt = models.IntegerField()
    image = models.ImageField(upload_to='images/')

class StatisticDocument(models.Model):
    bibliotheque = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE)
    idDocument = models.AutoField(primary_key=True)
    dateDocumentStatistique = models.DateField()
    lienDocument = models.URLField()
