from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.RegisterView.as_view(), name='register'),
    path('users/login/', views.LoginView.as_view(), name='login'),
    path('users/current/', views.UserView.as_view(), name='current'),
    path('users/logout/', views.LogoutView.as_view(), name='logout')
]