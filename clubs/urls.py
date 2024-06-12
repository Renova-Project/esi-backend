from django.urls import path
from .views import  ClubViewSet , ClubDetailAPIView , EventCreateView, ClubCreateView

urlpatterns = [
    path('clubs/', ClubViewSet.as_view(), name='clubs home page'),
    path('clubs/<int:id>/', ClubDetailAPIView.as_view(), name='club detail page'),
    #    path('clubs/<int:club_id>/upcoming-events/', UpcomingEventsView.as_view(), name='upcoming-events'),
    path('club/event/create', EventCreateView.as_view(), name='club_event_create' ), 
    path('club-register/', ClubCreateView.as_view(), name='club_registration' ),
]
