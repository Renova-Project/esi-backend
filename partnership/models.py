from django.db import models



# Model representing the SectorActivity table
class SectorActivity(models.Model):
    sectorId = models.AutoField(primary_key=True)  # Equivalent to SERIAL
    sectorName = models.CharField(max_length=100)  # VARCHAR(100)

    def __str__(self):
        return self.sectorName


class Partner(models.Model):
    organizationName = models.CharField(max_length=255)  
    organizationDescription = models.TextField()  
    organizationAddress = models.TextField()  
    organizationEmail = models.EmailField(max_length=255)  
    organizationPhone = models.CharField(max_length=20)  
    organizationSize = models.IntegerField()  
    organizationCountry = models.CharField(max_length=50)  
    websiteLink = models.URLField()  
    organizationLogo =models.ImageField(upload_to="partnership/logos/")

    officialDocument = models.FileField(upload_to="partnership/official_documents")

    sectorActivity = models.ForeignKey(
        SectorActivity,
        on_delete=models.CASCADE, 
        related_name="partners",
    )

    def __str__(self):
        return self.organizationName
