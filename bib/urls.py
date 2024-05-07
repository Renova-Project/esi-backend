from django.urls import path
from . import views

urlpatterns = [
    # Oeuvre
    path('oeuvres/', views.OeuvreListCreate.as_view(), name='oeuvre-list-create'),
    path('oeuvres/<int:pk>/', views.OeuvreRetrieveUpdateDestroy.as_view(), name='oeuvre-detail'),

    # StatisticDocument
    path('documents/', views.StatisticDocumentListCreate.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', views.StatisticDocumentRetrieveUpdateDestroy.as_view(), name='document-detail'),

    #searching
    path('search/', views.SearchView.as_view(), name='search'),
]