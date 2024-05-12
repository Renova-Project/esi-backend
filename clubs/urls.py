from django.urls import path
from .views import  ClubViewSet , ClubDetailAPIView

urlpatterns = [
    path('clubs/', ClubViewSet.as_view(), name='clubs home page'),
    path('clubs/<int:id>/', ClubDetailAPIView.as_view(), name='club detail page'),
]
