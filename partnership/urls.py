from django.urls import path
from .views import partners_view  , CoursesView

urlpatterns = [
    path('partners/',partners_view, name='partners page'),
    path('courses/',CoursesView.as_view(), name='diplomes'),
]