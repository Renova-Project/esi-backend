from django.db import models
from users.models import User

# Create your models here.

SPECIALTY_CHOICES = [
    ('SIT', 'SIT'),
    ('SIL', 'SIL'),
    ('SIQ', 'SIQ'),
    ('SID', 'SID'),
]


class Institution(models.Model): #etablissement
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100 )

class Teacher(models.Model) : 
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    rank = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    is_researcher = models.BooleanField(default=False)
    specialty = models.CharField(max_length=100,choices=SPECIALTY_CHOICES)
    office = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teachers/')    

class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

class PhDStudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    thesis_title = models.CharField(max_length=255)
    supervisor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    starting_date = models.DateField()
    defense_date = models.DateField()
    

class Lab(models.Model):
    name = models.CharField(max_length=255) # to be change to selection
    description = models.TextField()
    theme = models.CharField(max_length=255)
    creation_date = models.DateField() 
    logo =  models.ImageField(upload_to='labs/')
    
    
class Theme(models.Model):
    name = models.CharField(max_length=100)
    designation = models.TextField()

class ResearchTeam(models.Model):
    name = models.CharField(max_length=255)
    cheif_researcher = models.ForeignKey(Teacher , on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    
class TeamMemberShip(models.Model): 
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    research_team = models.ForeignKey(ResearchTeam, on_delete=models.CASCADE)
    date_joined = models.DateField()

class ResearchProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_national = models.BooleanField()
    team = models.ForeignKey(ResearchTeam, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    starting_date = models.DateField()
    

# it research project with techers 


# many to many with research project 
   
class Publication(models.Model): # f site
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    attachment = models.FileField(upload_to='attachments/')
    date = models.DateField()



class Training(models.Model): #formation
    trainer  = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    training_title = models.CharField(max_length=255)
    training_date = models.DateField()


class Link(models.Model):
    url = models.URLField()
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

class PermanentMember(models.Model):
    team = models.ForeignKey(ResearchTeam, on_delete=models.CASCADE)
    allocation_date = models.DateField()

class NonPermanentMember(models.Model):
    team = models.ForeignKey(ResearchTeam, on_delete=models.CASCADE)
    allocation_date = models.DateField()

class Collaborator(models.Model):
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()


#class Student(models.Model):
#    is_permanent = models.BooleanField()


class Intern(models.Model):
    internship_title = models.CharField(max_length=255)

class ResearchSupervisor(models.Model):
    supervisor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    allocation_date = models.DateField()

class ResearchTask(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(ResearchSupervisor, on_delete=models.CASCADE)
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)


class HasTheme(models.Model):
    project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
