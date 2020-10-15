from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<unique_id>', views.update, name='update'),
    path('sightings/add', views.add, name='add'),
    path('sightings/stats', views.stats, name='stats'),
    path('map/', views.map, name='map'),
]
