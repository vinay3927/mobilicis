from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .scripts.scraping import scrape_property_details
 

@csrf_exempt
def scrape_properties(request):
    if request.method == 'POST':
        cities = ["Pune", "Delhi", "Mumbai", "Lucknow", "Agra", "Ahmedabad", "Kolkata", "Jaipur", "Chennai", "Bengaluru"]
        for city in cities:
            scrape_property_details(city)

        return JsonResponse({'message': 'Scraping process initiated successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
    