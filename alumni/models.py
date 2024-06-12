from django.db import models

# Create your models here.


class Alumni(models.Model) : 
    
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    defense_year = models.CharField(max_length=4) 
    speciality = models.CharField(max_length=100)
    current_position = models.CharField(max_length=100)
    testimony = models.TextField()
    testimony_rating = models.IntegerField()
    is_validated = models.BooleanField(default=False)
    





    #contacts 
    
    '''
    anneeDeSoutenance
    specialite 
    postActuel
    contactLinks(fk)
    temoignage
    temoignageRating
    ''' 
    
    

    