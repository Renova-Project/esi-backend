from django.db import models
from school.models import Event

# Create your models here.

class Club(models.Model):
    #club_mail = models.EmailField() #to be changed when user model
    #idPresident = models.ForeignKey(User, on_delete=models.CASCADE)  #add student foreign key
    club_name = models.CharField(max_length=100, null=True) #to be changed when user model is created
    logo = models.ImageField(upload_to='clubs/logo/')  
    description = models.TextField()
    domain = models.CharField(max_length=100, null=True)
    opening_date = models.DateField()  
    major_event = models.CharField(max_length=100, null=True) 
    
    member_count = models.IntegerField()  
    event_count = models.IntegerField()
    
    phone_number =models.CharField(max_length=15, null=True)
    #socila media links 
    website_link = models.URLField(null=True)
    facebook_link = models.URLField(null=True)
    instagram_link = models.URLField(null=True)
    linkedin_link = models.URLField(null=True)
    youtube_link = models.URLField(null=True)
    twitter_link = models.URLField(null=True)
    discord_link = models.URLField(null=True)
        

class ClubEventExperience (models.Model) :
    
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    experience = models.TextField()
    rating = models.IntegerField()
    date = models.DateField()
    # add student  foreign key
    
    


    
    

    
    
    



