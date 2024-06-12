from django.contrib import admin
from .models import Teacher , Institution ,Lab , ResearchTeam , ResearchProject

# Register your models here.


class TeacherAdmin(admin.ModelAdmin) : 
    list_display =[ 'teacher_image','get_first_name','get_last_name','email', 'office', 'specialty']

    search_fields =[ 'speciality' , 'office']
    actions = None
    
    
    def get_first_name(self, obj) : 
        return obj.user.first_name
    get_first_name.short_description = 'First Name'
        
    def get_last_name(self, obj) : 
        return obj.user.last_name   
    get_last_name.short_description = 'Last Name'
    
    def teacher_image(self, obj):
        if obj.image:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No Image"
    teacher_image.short_description = 'Image'
    
    

class InstitutionAdmin(admin.ModelAdmin) : 
    list_display =[ 'name','country']

    search_fields =[ 'name' , 'country']
    actions = None
    
    
class ResearchTeamAdmin(admin.ModelAdmin) : 
    list_display =[ 'name','get_cheif_researcher','get_theme_name']
    
    def get_theme_name(self, obj) : 
        return obj.theme.name
    get_theme_name.short_description = 'Theme'
        
    def get_cheif_researcher(self, obj) : 
        return obj.cheif_researcher.user.first_name   
    get_cheif_researcher.short_description = 'Cheif Researcher'

    search_fields =[ 'name']
    actions = None
    
    
class ResearchProjectAdmin(admin.ModelAdmin) :
    list_display = ['title','is_national' , 'lab' , 'get_team' ]
    
    def get_team(self , obj) : 
        return obj.team.name


    

admin.site.register(Teacher ,TeacherAdmin)
admin.site.register(Institution ,InstitutionAdmin)
admin.site.register(ResearchTeam , ResearchTeamAdmin)
admin.site.register(ResearchProject ,ResearchProjectAdmin )



