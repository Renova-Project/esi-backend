from django.urls import path
from .views import  EventListView, NewsByTypeView ,HomeView 

urlpatterns = [
    path('home/', HomeView.as_view(), name='home page'),
    path('events/', EventListView.as_view(), name='event_list'), 
    path('news/', NewsByTypeView.as_view(), name='news-by-type'),
]
