from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Sightings

def homepage(request):
    return render(request, 'sqtracker/homepage.html', {})

def sightings(request):
    Sightings = Sightings.object.all()
    context = {
        'Sighting': Sightings
    }
    return render (request, 'sqtracker/sightings.html', context)

def update(request, unique_id):
    obj = get_object_or_404(Sightings, unique_squirrel_id=unique_id)
    
