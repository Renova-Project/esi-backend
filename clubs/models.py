from django.db import models

# Create your models here.

class Club(models.Model):
    nomClub = models.CharField(max_length=255) #coming from  the default user
    emailClub = models.EmailField()  #comming from the default user
    openingDate = models.DateField()  
    logo = models.ImageField( null=False, upload_to='clubs/logo/')  
    #idPresident = models.ForeignKey(User, on_delete=models.CASCADE)  
    memberCount = models.IntegerField()  
    eventCount = models.IntegerField()
    events = models.ManyToManyField('events.Event', related_name='events')
    
    

    def __str__(self):
        return self.nomClub
    
    
    



