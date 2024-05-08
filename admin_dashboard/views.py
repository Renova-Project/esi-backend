from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

from django.contrib.auth import views as auth_views
from school.models import SchoolGallery
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status




# Create your views here.

def index(request):
  return render(request, 'pages/index.html')


# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/register.html', context)

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/login.html'
  form_class = LoginForm
  def get_success_url(self):
      return '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')



def school_gallery_view(request):
    
    context = {
      'images': SchoolGallery.objects.all(),
      'base_url': 'https://res.cloudinary.com/derk6emxa/image/upload/v1/'
    }
    return render(request, 'pages/school_gallery.html', context)
  
  
#need csrf token
@api_view(["DELETE"])  # Allows only DELETE requests  
def delete_image_view(request, image_id):
  try:
      image = SchoolGallery.objects.get(id=image_id)
      image.delete()
      return JsonResponse({'status': 'success'})
  except SchoolGallery.DoesNotExist:
      return JsonResponse({'error': 'Image not found'},status=status.HTTP_404_NOT_FOUND)