from django.shortcuts import render

def home(request):
    return render(request, 'places/home.html')

def park(request):
    return render(request, 'places/park.html')

def school(request):
    return render(request, 'places/school.html')

def church(request):
    return render(request, 'places/church.html')

def turf(request):
    return render(request, 'places/turf.html')

def apartments(request):
    return render(request, 'places/apartments.html')
