from django.contrib import admin
from .models import Bibliotheque, Directeur, Oeuvre, StatisticDocument

admin.site.register(Bibliotheque)
admin.site.register(Directeur)
admin.site.register(Oeuvre)
admin.site.register(StatisticDocument)
