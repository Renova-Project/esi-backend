from django.urls import path
from .views import  ClubViewSet

urlpatterns = [
    path('clubs/', ClubViewSet.as_view(), name='clubs home page'),
]
