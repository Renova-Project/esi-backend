from django.contrib import admin
from django.utils.html import format_html
from .models import Slider, Event,News ,SchoolGallery ,SuccessStory, Defense, Conference, Competition, Examiner, Speaker


class SliderAdmin(admin.ModelAdmin):
    
    list_display = ('custom_slider_description', 'custom_slider_action_name', 'custom_slider_link', 'slider_image_thumbnail')
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
    
class EventAdmin(admin.ModelAdmin):
    list_display = [ 'event_name', 'start_date', 'end_date']

    search_fields = ['event_name']  
    list_filter = ['start_date']  
    
    actions = None
    
# Custom admin class
#class SchoolGalleryAdmin(admin.ModelAdmin):
#    list_display = ['thumbnail']  # Display these fields in the list view
#    changelist_template = "admin/school/schoolgallery_grid_changelist.html"

    
    def thumbnail(self, obj):
        if obj.link_image:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.link_image.url}" style="width: 100px; height: auto;" />')
        return "No Image"
    thumbnail.short_description = 'Image'
    
    actions =None
    
        
class NewsAdmin(admin.ModelAdmin):
    # Instead of displaying 'news_date' directly, use custom methods for date and time
    list_display = ['news_name', 'news_date_display', 'news_time_display', 'thumbnail_news']
    search_fields = ('news_name', 'news_details')
    ordering = ('-news_date',) 

    def news_date_display(self, obj):
        return obj.news_date.strftime('%Y-%m-%d')
    news_date_display.short_description = 'News Date'

    def news_time_display(self, obj):
        return obj.news_date.strftime('%H:%M:%S')
    news_time_display.short_description = 'News Time'

    def thumbnail_news(self, obj):
        if obj.image:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />')
        return "No Image"
    thumbnail_news.short_description = 'Thumbnail'

    actions = None

    
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ['shortened_title', 'thumbnail']  
    
    def shortened_title(self, obj):
        if len(obj.title) > 60:
            return obj.title[:60] + ' ...'
        else:
            return obj.title
    shortened_title.short_description = 'Title'
    
    def thumbnail(self, obj):
        if obj.image:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" style="width: 50px; height: 50px;" />')
        return "No Image"
    thumbnail.short_description = 'Image'
    
    actions =None
    

 

# Register the model with the custom admin class
#admin.site.register(SchoolGallery, SchoolGalleryAdmin)

admin.site.register(SchoolGallery)
admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(SuccessStory, SuccessStoryAdmin)
