from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('schoolgallery/', views.school_gallery_view, name='school_gallery'),
    path('delete_image/<int:image_id>/', views.delete_image_view, name='delete_image'),
 
    
    path('club_event_validation/', views.club_event_validation_view, name='club_event_validation'),
    path('partnership_request_validation/', views.partnership_request_view, name='partnership_request_validation'),
    path('success_stories_validation/', views.success_stories_validation_view, name='success_stories_validation'),
    path('alumni_testimony_validation/', views.alumni_testimony_validation_view, name='alumni_testimony_validation'),
    path('diplome_validation/', views.diplome_validation_view, name='diplome_validation'),
    
    path('validate_partner/', views.validate_partner, name='validate_partner'),
    path('validate_success_story/', views.validate_success_story, name='validate_success_story'),
    path('validate_club_event/', views.validate_club_event, name='validate_club_event'),
    path('validate_testimony/', views.validate_testimony, name='validate_testimony'),
    
    path('validate_diplome/', views.validate_diplome, name='validate_diplome'),




    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login_user'),
    path('accounts/logout/', views.user_logout_view, name='logout_user'),#to be changed
    path('accounts/register/', views.registration, name='register_user'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),# to be changed
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
