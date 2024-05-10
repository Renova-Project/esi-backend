from django.db import models

# Model representing a Module
class Module(models.Model):
    module_name = models.CharField(max_length=25)  # module_name
    designation = models.CharField(max_length=255)  # designation
    coef = models.IntegerField()  # coef
    volume_cours = models.FloatField()  # volume_cours
    volume_td = models.FloatField()  # volume_td
    objectif = models.TextField()  # objectif
    prerequis= models.ManyToManyField('Prerequis', blank=True)
    

# Model representing a Chapitre
class Chapitre(models.Model):
    num = models.IntegerField()  # num
    chapitre_name = models.CharField(max_length=255)  # chapitre_name
    chapitre_description = models.TextField()  # chapitre_description
    module = models.ForeignKey(Module, related_name='chapitres', on_delete=models.CASCADE)  # Each Chapitre belongs to one Module


# Model representing a Specialité
class Specialite(models.Model):
    nomspecialite = models.CharField(max_length=255)  # nomspecialite
    designation = models.CharField(max_length=255)  # designation
    LifeAs = models.TextField()  # LifeAs a student of this field a long description
    Image = models.ImageField(upload_to='images/')  # Image
    videoLink = models.URLField()  # videoLink
    ModulesS1 = models.ManyToManyField(Module, related_name='specialite_s1')  # ModulesS1
    ModulesS2 = models.ManyToManyField(Module, related_name='specialite_s2')  # ModulesS2
    skills = models.ManyToManyField('Skills', related_name='specialites')  # skills
    pdfFile = models.FileField(upload_to='pdfs/')  # pdfFile


# skills of a specific field(specialite)
class Skills(models.Model):
    skill= models.CharField(max_length=255) 
    description=models.TextField() # descriptionskill


# Model representing AnnéeEtude
class AnneeEtude(models.Model):
    codeAnnée = models.IntegerField()  # codeAnnée
    designation = models.CharField(max_length=255)  # designation
    description = models.TextField()  # description

# Model representing SousObjectifs
class SousObjectif(models.Model):
    text = models.TextField()  # text
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='sousobjectifs')  # Each SousObjectif corresponds to one Module

# Model representing Bibliographie
class Bibliographie(models.Model):
    textreference = models.TextField()  # textreference
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='bibliographies')  # Each Bibliographie corresponds to one Module

    
from django.db import models

# Model representing Competances
class Competances(models.Model):
    familleCompetence = models.ForeignKey('FamilleCompetence', on_delete=models.CASCADE)  # familleCompetence
    codeCompetence = models.CharField(max_length=255)  # nomCompetence
    designationCompetence = models.CharField(max_length=255)  # designationCompetence

    def __str__(self):
        return self.nomCompetence

# Model representing FamilleCompetence
class FamilleCompetence(models.Model):
    codeFamille = models.IntegerField()  # codeFamille
    designation = models.CharField(max_length=255)  # designation

    def __str__(self):
        return self.designation

# Model representing ElementCompetences
class ElementCompetences(models.Model):
    codeElmcompetence = models.IntegerField()  # codeElmcompetence
    designation = models.CharField(max_length=255)  # designation
    Niveau_choices = (
        ('base', 'Base'),
        ('intermediaire', 'Intermédiaire'),
        ('avancé', 'Avancé'),
    )
    niveau = models.CharField(max_length=15, choices=Niveau_choices)  # Niveau
    competence = models.ForeignKey(Competances, on_delete=models.CASCADE, related_name='elementsCompetences')  # ForeignKey to Competances

    def __str__(self):
        return self.designation


# Model representing Prerequis
class Prerequis(models.Model):
    Text = models.TextField()  # Text
       
    
class Job(models.Model):
    nom_job = models.TextField() #nom_job
    description = models.TextField() # Description  
    image = models.ImageField(upload_to="studies/jobs/")
    Specialite = models.ForeignKey('Specialité', on_delete=models.CASCADE, related_name='jobs')  # Each Bibliographie corresponds to one Module



