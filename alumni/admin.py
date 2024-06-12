from django.contrib import admin
from .models import Alumni

class AlumniAdmin(admin.ModelAdmin):
    list_display = ('user_first_name', 'user_last_name', 'short_testimony')

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'First Name'

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'Last Name'

    def short_testimony(self, obj):
        return (obj.testimony[:197] + '...') if len(obj.testimony) > 200 else obj.testimony
    short_testimony.short_description = 'Testimony'

admin.site.register(Alumni, AlumniAdmin)