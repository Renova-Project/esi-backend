from django.db import models



# Model representing the SectorActivity table
class SectorActivity(models.Model):
    sectorId = models.AutoField(primary_key=True)  # Equivalent to SERIAL
    sectorName = models.CharField(max_length=100)  # VARCHAR(100)

    def __str__(self):
        return self.sectorName


# Model representing the Partner table with a foreign key reference to SectorActivity
class Partner(models.Model):
    organizationId = models.AutoField(primary_key=True)  # Equivalent to SERIAL
    organizationName = models.CharField(max_length=255)  # VARCHAR(255)
    organizationDescription = models.TextField()  # TEXT
    organizationAddress = models.TextField()  # TEXT
    organizationEmail = models.EmailField(max_length=255)  # VARCHAR(255)
    organizationPhone = models.CharField(max_length=20)  # VARCHAR(20)
    organizationSize = models.IntegerField()  # INTEGER
    organizationCountry = models.CharField(max_length=50)  # VARCHAR(50)
    websiteLink = models.URLField()  # TEXT
    organizationLogo =models.ImageField(upload_to="partnership/logos/")

    officialDocument = models.FileField(upload_to="partnership/official_documents")

    sectorActivity = models.ForeignKey(
        SectorActivity,
        on_delete=models.CASCADE,  # Corresponds to the FOREIGN KEY relationship
        related_name="partners",
    )

    def __str__(self):
        return self.organizationName
