from django.contrib import admin

# Register your models here.
# admin.py
from .models import Slider, Image, Event, News, Defense, Conference, Competition, Examiner, Speaker

admin.site.register(Image)
admin.site.register(Event)
admin.site.register(News)
#admin.site.register(Defense)
#admin.site.register(Conference)
#admin.site.register(Competition)
#admin.site.register(Examiner)
#admin.site.register(Speaker)




# Define the SliderAdmin class to customize admin functionalities for the Slider model
class SliderAdmin(admin.ModelAdmin):
    
    
    # This list will show these fields in the list view in the admin interface
    list_display = ('custom_slider_description', 'custom_slider_action_name', 'custom_slider_link', 'slider_image_thumbnail')


    # Enable search on specific fields
    search_fields = ('slider_description', 'slider_action_name')  # Search by these fields

    def custom_slider_description(self, obj):
        return obj.slider_description
    custom_slider_description.short_description = "Description"

    def custom_slider_action_name(self, obj):
        return obj.slider_action_name
    custom_slider_action_name.short_description = "Action"

    def custom_slider_link(self, obj):
        return obj.slider_link
    custom_slider_link.short_description = "Link"

    # Custom function to create a thumbnail for the image
    def slider_image_thumbnail(self, obj):
        if obj.slider_image:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.slider_image.url}" width="50" height="50" />')
        return "No Image"
    slider_image_thumbnail.short_description = 'Image'
    
    actions = None

# Register the Slider model with its admin class
admin.site.register(Slider, SliderAdmin)
