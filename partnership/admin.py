from django.contrib import admin
from django.utils.html import mark_safe
from .models import Partner, SectorActivity , Diplome


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['partner_image', 'name', 'email', 'country', 'sector_of_activity']
    
    def sector_of_activity(self, obj):
        return obj.sectorActivity.sectorName
    sector_of_activity.short_description = 'Sector of Activity'
    
    def partner_image(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="50" height="50" />')
        return "No Image"
    partner_image.short_description = 'Image'
    
    actions = None

admin.site.register(Partner, PartnerAdmin)
admin.site.register(SectorActivity)
admin.site.register(Diplome)
