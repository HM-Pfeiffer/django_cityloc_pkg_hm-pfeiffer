from django.shortcuts import render

# Create your views here.
def loc_nyc(request):
    return render(request, 'citylocations/loc_nyc.html', {})

