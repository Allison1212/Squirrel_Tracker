from django.forms import ModelForm
from .models import Sightings

class Form(ModelForm):
    class Meta:
        model = Sightings
        fields = '__all__'

class Partial(ModelForm):
    class Meta:
        model = Sightings
        fields = ['latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age']
