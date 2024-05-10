from django.db import models
from school.models import Event

# Create your models here.

class Club(models.Model):
    club_name = models.CharField(max_length=100, null=True) #to be changed when user model is created
    logo = models.ImageField(upload_to='clubs/logo/')  
    #idPresident = models.ForeignKey(User, on_delete=models.CASCADE)  #add student foreign key
    member_count = models.IntegerField()  
    event_count = models.IntegerField()
    description = models.TextField()
    opening_date = models.DateField()  



class ClubEventExperience (models.Model) :
    
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    experience = models.TextField()
    rating = models.IntegerField()
    date = models.DateField()
    # add student  foreign key
    
    
    
    

    
    
    



