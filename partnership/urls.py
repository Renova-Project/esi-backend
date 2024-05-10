from django.urls import path
from .views import partners_view 

urlpatterns = [
    path('partners/',partners_view, name='partners page'),
]