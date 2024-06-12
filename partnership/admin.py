from django.contrib import admin
from django.utils.html import mark_safe
from .models import Partner, SectorActivity , Diplome , Courses


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
    
    
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date_range', 'price', 'level', 'rate', 'course_image']
    actions = None
    
    def course_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.logo.url}" width="80" height="80" />')
        return "No Image"

    course_image.short_description = 'Image'

admin.site.register(Partner, PartnerAdmin)
admin.site.register(SectorActivity)
admin.site.register(Diplome)

admin.site.register(Courses ,CourseAdmin )
