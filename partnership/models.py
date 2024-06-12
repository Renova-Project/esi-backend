from django.db import models



# Model representing the SectorActivity table
class SectorActivity(models.Model):
    sectorId = models.AutoField(primary_key=True)  # Equivalent to SERIAL
    sectorName = models.CharField(max_length=100)  # VARCHAR(100)

    def __str__(self):
        return self.sectorName


class Partner(models.Model):
    name = models.CharField(max_length=255)  
    description = models.TextField()  
    address = models.TextField()  
    email = models.EmailField(max_length=255)  
    phone = models.CharField(max_length=20)  
    size = models.IntegerField()  
    country = models.CharField(max_length=50)  
    link = models.URLField()  
    logo =models.ImageField(upload_to="partnership/logos/")

    official_document = models.FileField(upload_to="partnership/official_documents")
    
    is_validated = models.BooleanField(default=False)

    sectorActivity = models.ForeignKey(
        SectorActivity,
        on_delete=models.CASCADE, 
        related_name="partners",
    )
    
class Diplome(models.Model) : 
    image =models.ImageField(upload_to="partner/dimplomes/")
    partner = models.ForeignKey(Partner , on_delete=models.CASCADE)
    is_validated = models.BooleanField(default=None)


