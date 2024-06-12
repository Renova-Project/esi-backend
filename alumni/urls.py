from django.urls import path
from .views import  AlumniTestimonyView , PostTestimonyView

urlpatterns = [
    path('alumni/testimonies/', AlumniTestimonyView.as_view(), name='testtimonies page'),
    path('alumni/testimonies/post', PostTestimonyView.as_view(), name='testtimonies page'),
]

