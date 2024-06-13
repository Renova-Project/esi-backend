from django.urls import path
from .views import  EventListView, NewsByTypeView ,HomeView ,SearchView, SuccessStroriesView ,SchoolGalleryView , SuccessStoryDetail ,EventDetailView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home page'),
    path('events/', EventListView.as_view(), name='event_list'), 
    
    path('events/<int:id>/', EventDetailView.as_view(), name='event_by_id'), 

    path('news/', NewsByTypeView.as_view(), name='news-by-type'),
    path('search/', SearchView.as_view(), name='search'),
    path("stories/", SuccessStroriesView.as_view(), name="success-stories"), 
    path("stories/<int:id>/", SuccessStoryDetail.as_view(), name="story-detail"), 
    
    path('school/gallery/', SchoolGalleryView.as_view(), name="school images")
]
