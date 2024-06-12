from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from users.models import User

class Slider(models.Model):
    slider_image = models.ImageField(upload_to="school/slider/")
    slider_description = models.CharField(max_length=255)
    slider_action_name = models.CharField(max_length=100)
    slider_link = models.URLField(blank=True)
    
    
class SchoolGallery(models.Model):
    image_description = models.TextField()
    link_image = models.ImageField(upload_to="school/gallery/")
    
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_type = models.TextField()
    event_description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_details = models.TextField()
    event_location = models.TextField()
    
    is_validated = models.BooleanField(default=False)
    image = models.ImageField(upload_to="school/events/images", null=True, blank=True)
    
    event_maker = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    #image = models.ForeignKey('Image', on_delete=models.CASCADE) #indicate one associated image
    

class SuccessStory(models.Model) : 
    
    image =models.ImageField(upload_to="school/success_stories")
    title = models.CharField(max_length=255)
    description =models.TextField()
    story_date =models.DateField()
    
    is_validated = models.BooleanField(default=False)
    
class SchoolStatistic(models.Model) : 
    designation = models.CharField(max_length=255)
    number = models.IntegerField()
     

class News(models.Model):
    NEWS_TYPE_CHOICES = (
        ('INSIDE', 'something done inside the school'),
        ('OUTSIDE', 'something done outside the school'),
    )
    news_name = models.CharField(max_length=50)
    news_type = models.CharField(max_length=20, choices=NEWS_TYPE_CHOICES)
    news_details = models.TextField()
    news_date = models.DateTimeField()
    image = models.ImageField(upload_to="school/images/")

class Defense(models.Model): 
    event = models.OneToOneField('Event', on_delete=models.CASCADE)
    theme = models.TextField()
    field = models.TextField()
    organizer = models.ForeignKey('Examiner', on_delete=models.CASCADE)
    defense_date = models.DateTimeField()

class Conference(models.Model):
    event = models.OneToOneField('Event', on_delete=models.CASCADE)
    conference_theme = models.TextField()
    conference_date = models.DateTimeField()
    organizer = models.ForeignKey('Examiner', on_delete=models.CASCADE)

class Competition(models.Model):
    event = models.OneToOneField('Event', on_delete=models.CASCADE)
    competition_theme = models.TextField()
    link_competition = models.URLField(blank=True)


class Examiner(models.Model):
    examiner_last_name = models.TextField()
    examiner_first_name = models.TextField()
    profession = models.TextField()
    organization = models.TextField()

class Speaker(models.Model):
    speaker_last_name = models.CharField(max_length=50)
    speaker_first_name = models.CharField(max_length=50)
    profession = models.TextField()
    organization = models.TextField()