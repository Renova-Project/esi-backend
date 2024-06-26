from django.urls import path
from .views import  EventListView, NewsByTypeView ,HomeView ,SearchView, SuccessStroriesView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home page'),
    path('events/', EventListView.as_view(), name='event_list'), 
    path('news/', NewsByTypeView.as_view(), name='news-by-type'),
    path('search/', SearchView.as_view(), name='search'),
    path("stories/", SuccessStroriesView.as_view(), name="success-stories")
]
