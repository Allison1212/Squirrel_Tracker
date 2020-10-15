from django.db import models
from django.utils.translation import gettext as _

class Sightings(models.Model):
    # Latitude
    latitude = models.CharField(
        max_length = 20,
    )

    #Longitude
    longitude = models.CharField(
        max_length = 20,
    )

    #Unique Squirrel ID
    unique_squirrel_id = models.CharField(
        max_length = 20,
    )

    #Shift
    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM,_('AM')),
        (PM,_('PM')),
    ]
    shift = models.CharField(
        max_length = 2,
        choices = SHIFT_CHOICES,
        default = AM,
    )

    #Date
    date = models.DateField(
        help_text = _('Date'),
    )

    #Age
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = [
        (ADULT,_('Adult')),
        (JUVENILE,_('Juvenile')),
    ]

    age = models.CharField(
        max_length = 20,
        choices = AGE_CHOICES,
        default = JUVENILE,
        )

    # Primary Fur Color
    primary_fur_color = models.CharField(
        max_length = 20,
    )

    #Location
    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'

    LOCATION_CHOICES = [
        (GROUND_PLANE,_('Ground Plane')),
        (ABOVE_GROUND,_('Above Ground')),
        ]
    location = models.CharField(
        max_length = 20,
        choices = LOCATION_CHOICES,
        default = GROUND_PLANE,
        )

    #Specific Location
    specific_location = models.CharField(
        max_length = 50,
    )

    # Running
    running = models.BooleanField()

    # Chasing
    chasing = models.BooleanField()

    # Climbing
    climbing = models.BooleanField()

    # Eating
    eating = models.BooleanField()

    # Foraging
    foraging = models.BooleanField()

    # Other Activities
    other_activities = models.CharField(
        max_length = 100,
    )

    # Kuks
    kuks = models.BooleanField()

    # Quaas
    quaas = models.BooleanField()

    # Moans
    moans = models.BooleanField()

    # Tail flags
    tail_flags = models.BooleanField()

    # Tail twitches
    tail_twitches = models.BooleanField()

    # Approaches
    approaches = models.BooleanField()

    # Indifferent
    indifferent = models.BooleanField()

    # Runs from
    runs_from = models.BooleanField()

    def __str__(self):
        return self.unique_squirrel_id
