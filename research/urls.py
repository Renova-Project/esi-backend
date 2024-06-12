from django.urls import path
from .views import DirectoryOfResearcherView , ResearcherDetailView

urlpatterns = [
    path('researchers/', DirectoryOfResearcherView.as_view(), name='Directory of Researchers'),
    path('researcher/<int:id>/', ResearcherDetailView.as_view(), name='Researcher Detail'),
]
