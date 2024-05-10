from django.http import JsonResponse

# Create your views here.
def partners_view(request):
    partners = [
        {'name': 'Partner 1', 'location': 'Location 1'},
        {'name': 'Partner 2', 'location': 'Location 2'},
        {'name': 'Partner 3', 'location': 'Location 3'},
    ]
    
    return JsonResponse({'partners': partners})