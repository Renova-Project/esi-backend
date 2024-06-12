from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

from django.contrib.auth import views as auth_views
from school.models import SchoolGallery
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from school.models  import Event , SuccessStory
from partnership.models import Partner
from alumni.models import Alumni 
from partnership.models import Diplome
from django.shortcuts import redirect, get_object_or_404

from django.core.mail import send_mail



BASE_URL = 'https://res.cloudinary.com/derk6emxa/image/upload/v1/'


# Create your views here.

def index(request):
  return render(request, 'pages/index.html')


def chat_view(request):
  return render(request, 'pages/chat_front.html')


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
      'base_url': BASE_URL
    }
    return render(request, 'pages/school_gallery.html', context)
  
  
def alumni_testimony_validation_view(request):
  #get all not validated club events 
  #get all updated club events , that existe  and validated recently
  #dont forget to update  - we must show club event and not all events 
  
  testimonies = Alumni.objects.filter(is_validated=False)
  context = {
    "non_validated_testimonies": testimonies,
    'base_url': BASE_URL
  }
  return render(request, 'pages/alumni_testimony_validation.html', context)  


def validate_testimony(request):
    if request.method == 'POST':
        testimony_id = request.POST.get('testimony_id')
        testimony = get_object_or_404(Partner, pk=testimony_id)
        testimony.is_validated = True
        testimony.save()
        
    return render(request ,'pages/alumni_testimony_validation.html')
  
  
def club_event_validation_view(request):
  #get all not validated club events 
  #get all updated club events , that existe  and validated recently
  #dont forget to update  - we must show club event and not all events 
  
  non_validated_events = Event.objects.filter(is_validated=False)
  context = {
    "non_validated_events_list": non_validated_events,
    'base_url': BASE_URL
  }
  return render(request, 'pages/club_event_validation.html', context)

def validate_club_event(request):
    if request.method == 'POST':
        club_event_id = request.POST.get('club_event_id')
        club_event = get_object_or_404(Partner, pk=club_event_id)
        club_event.is_validated = True
        club_event.save()
        
    return render(request ,'pages/club_event_validation.html')


def partnership_request_view(request):

  non_validated_events = Partner.objects.filter(is_validated=False)
  
  for event in non_validated_events:
    print("official document",event.official_document)
  
  context = {
    "partnership_request_list": non_validated_events,
    'base_url': BASE_URL
  }
  return render(request, 'pages/partnership_request_validation.html', context)

def validate_partner(request):
    if request.method == 'POST':
        partner_id = request.POST.get('partner_id')
        partner = get_object_or_404(Partner, pk=partner_id)
        partner.is_validated = True
        partner.save()
        
    return render(request ,'pages/partnership_request_validation.html')



def success_stories_validation_view(request):

  non_validated_stories = SuccessStory.objects.filter(is_validated=False)
  context = {
    "success_stories_list": non_validated_stories,
    'base_url': BASE_URL
  }
  return render(request, 'pages/success_stories_validation.html', context)


def validate_success_story(request):
    if request.method == 'POST':
        story_id = request.POST.get('story_id')
        story = get_object_or_404(Partner, pk=story_id)
        story.is_validated = True
        story.save()
        
    return render(request ,'pages/success_stories_validation.html')


def diplome_validation_view(request):
  diplomes = Diplome.objects.all()
  context = {
    "diplomes": diplomes,
    'base_url': BASE_URL
  }
  return render(request, 'pages/diplome_validation.html', context)  


def render_dashboard(request):
  
  partner_count = Partner.objects.count()
  
  return render(request, 'pages/dashboard.html')


def validate_diplome(request):
    if request.method == 'POST':
        validate_id = request.POST.get('validate_id')
        unvalidate_id = request.POST.get('unvalidate_id')

        diplome = get_object_or_404(Diplome, pk=validate_id)
        if validate_id:
          diplome.is_validated = True
        if unvalidate_id :
          diplome.is_validated = False

        diplome.save()
        
    return render(request ,'pages/diplome_validation.html')




#need csrf token
@api_view(["DELETE"])  # Allows only DELETE requests  
def delete_image_view(request, image_id): 
  try:
      image = SchoolGallery.objects.get(id=image_id)
      image.delete()
      return JsonResponse({'status': 'success'})
  except SchoolGallery.DoesNotExist:
      return JsonResponse({'error': 'Image not found'},status=status.HTTP_404_NOT_FOUND)