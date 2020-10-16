from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Sightings
from .form import Form,Partial

def homepage(request):
    return render(request, 'sqtracker/homepage.html', {})


def sightings(request):
    sightings = Sightings.objects.all()
    context = {
        'sightings': sightings
    }
    return render (request, 'sqtracker/sightings.html', context)

def update(request, unique_id):
    obj = get_object_or_404(Sightings, unique_squirrel_id=unique_id)
    form = Partial(request.POST or None, instance=obj)
    context = {'Partial': form}
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect('/sightings/')
    else:
        context = {
        'form' : form,
        }
        return render(request, 'sqtracker/update.html',context)

def add(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/sightings/')
    else:
        form = Form()
        context = {'form': form,}
        return render(request, 'sqtracker/add.html', context)

def stats(request):
    Number_of_Sightings = Sightings.objects.all().count()
    Number_of_Adults = Sightings.objects.filter(age = 'Adult').count()
    Number_of_Gray = Sightings.objects.filter(primary_fur_color = 'Gray').count()
    Number_of_Eating = Sightings.objects.filter(eating = True).count()
    Number_of_Climbing = Sightings.objects.filter(climbing = True).count()
    context = {
        'Number_of_Sightings': Number_of_Sightings,
        'Number_of_Adults': Number_of_Adults,
        'Number_of_Gray': Number_of_Gray,
        'Number_of_Eating': Number_of_Eating,
        'Number_of_Climbing': Number_of_Climbing,
    }
    return render(request, 'sqtracker/stats.html', context)

def map(request):
    sightings = Sightings.objects.all()
    context = {
        'sightings': sightings
    }
    return render(request, 'sqtracker/map.html', context)
