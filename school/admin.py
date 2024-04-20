from django.contrib import admin

# Register your models here.
# admin.py
from .models import Slider, Image, Event, News, Defense, Conference, Competition, Examiner, Speaker

admin.site.register(Slider)
admin.site.register(Image)
admin.site.register(Event)
admin.site.register(News)
admin.site.register(Defense)
admin.site.register(Conference)
admin.site.register(Competition)
admin.site.register(Examiner)
admin.site.register(Speaker)