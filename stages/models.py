from django.db import models

class Secteur(models.Model):
  nomSecteur = models.CharField(max_length=255)

  def __str__(self):
    return self.nomSecteur

class Partenaire(models.Model):
  secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
  nomPartenaire = models.CharField(max_length=255)

  def __str__(self):
    return self.nomPartenaire

class Organisme(models.Model):
  nomOrganisme = models.CharField(max_length=255)
  adresseOrganisme = models.CharField(max_length=255, blank=True)
  tailleOrganisme = models.CharField(max_length=255, blank=True)
  paysOrganisme = models.CharField(max_length=255, blank=True)
  emailOrganisme = models.EmailField(blank=True)
  telOrganisme = models.CharField(max_length=255, blank=True)
  logoOrganisme = models.ImageField(upload_to='logos/%Y/%m/%d', blank=True)
  domaine = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return self.nomOrganisme

class TypeStage(models.Model):
  nomType = models.CharField(max_length=255)
  descriptionType = models.TextField(blank=True)

  def __str__(self):
    return self.nomType

class Stage(models.Model):
  organisme = models.ForeignKey(Organisme, on_delete=models.CASCADE)
  nomStage = models.CharField(max_length=255)
  themeStage = models.CharField(max_length=255)
  descriptionStage = models.TextField()
  dureeStage = models.IntegerField()
  docteur = models.CharField(max_length=255)
  datePublication = models.DateField()
  typestage = models.ManyToManyField(TypeStage)

  def __str__(self):
    return self.nomStage

class Candidat(models.Model):
  nom = models.CharField(max_length=255)
  prenom = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

  def __str__(self):
    return f"{self.nom} {self.prenom}"

class Demande(models.Model):
  candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
  stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
  estAvere = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.candidat.nom} {self.candidat.prenom} - {self.stage.nomStage}"

# Optional model for OffreStage (if needed)
class OffreStage(models.Model):
  organisme = models.ForeignKey(Organisme, on_delete=models.CASCADE)
  # Add additional attributes specific to internship offers here (e.g., salaire, avantages)

  def __str__(self):
    return f"Offre de stage - {self.organisme.nomOrganisme}"
