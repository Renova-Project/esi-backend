from django.db import models

# Create your models here.

class Club(models.Model):
    #opening_date = models.DateField()  
    logo = models.ImageField(upload_to='clubs/logo/')  
    #idPresident = models.ForeignKey(User, on_delete=models.CASCADE)  
    member_count = models.IntegerField()  
    event_count = models.IntegerField()
    description = models.TextField()



class ClubEventExperience (models.Model) :
    
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    #event = models.ForeignKey('school.Event', on_delete=models.CASCADE)
    experience = models.TextField()
    rating = models.IntegerField()
    date = models.DateField()
    # add student  foreign key
    
    
    
    

    
    
    



