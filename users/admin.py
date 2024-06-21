from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    
    def name(self, obj):
        return obj.first_name + " " + obj.last_name
    name.short_description = "Name"

admin.site.register(User, UserAdmin)