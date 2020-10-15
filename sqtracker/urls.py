from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sightings/', views.index, name='index'),
    path('sightings/<unique_id>', views.index, name='index'),
    path('sightings/add', views.index, name='index'),
    path('sightings/stats', views.index, name='index'),
    path('map/', views.index, name='index'),
]
