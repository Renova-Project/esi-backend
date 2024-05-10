from django.contrib import admin
from .models import Club ,ClubEventExperience


class ClubEventExperienceAdmin(admin.ModelAdmin):
    list_display = ['get_club_name','get_event_name', 'rating', 'experience']
    list_filter = ['rating',]
    #search_fields = ['club_id', 'event_name', 'experience', 'date']
    
    def get_event_name(self, obj):
        return obj.event.event_name
    get_event_name.short_description = 'Event Name'
    
    def get_club_name(self, obj):
        return obj.club_id.club_name
    get_club_name.short_description = 'Club Name'
    
    actions = None
    
class ClubAdmin(admin.ModelAdmin):
    list_display = ['club_name', 'member_count', 'event_count','club_logo',]
    search_fields = ['club_name',]
    
    def club_logo(self, obj):
        if obj.logo:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.logo.url}" width="50" height="50" />')
        return "No Image"
    club_logo.short_description = 'Image'
    
    actions = None
    
admin.site.register(ClubEventExperience, ClubEventExperienceAdmin)
admin.site.register(Club, ClubAdmin)
