from django.contrib import admin

# Register your models here.

# Register your models here.
# admin.py
from .models import Partner , SectorActivity

admin.site.register(Partner)
admin.site.register(SectorActivity)

