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
        max_length = 16,
        choices = SHIFT_CHOICES,
        blank = True
    )

    #Date
    date = models.DateField(
        help_text = _('Date'),
        null = True,
        blank = True
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
        blank = True
        )

    # Primary Fur Color
    BLACK = 'Black'
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    COLOR_CHOICE=(
            (BLACK,_'Black'),
            (GRAY,_'Gray'),
            (CINNAMON,_'Cinnamon'),
            (None,_''),
            )
    primary_fur_color = models.CharField(
            max_length=16,
            choices = COLOR_CHOICE,
            blank = True
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
        blank = True
        )

    #Specific Location
    specific_location = models.CharField(
        max_length = 50,
        blank = True
    )

    # Running
    running = models.BooleanField(
        blank = True
    )

    # Chasing
    chasing = models.BooleanField(
        blank = True
    )

    # Climbing
    climbing = models.BooleanField(
        blank = True
    )

    # Eating
    eating = models.BooleanField(
        blank = True
    )

    # Foraging
    foraging = models.BooleanField(
        blank = True
    )

    # Other Activities
    other_activities = models.CharField(
        max_length = 100,
        blank = True
    )

    # Kuks
    kuks = models.BooleanField(
        blank = True
    )

    # Quaas
    quaas = models.BooleanField(
        blank = True
    )

    # Moans
    moans = models.BooleanField(
        blank = True
    )

    # Tail flags
    tail_flags = models.BooleanField(
        blank = True
    )

    # Tail twitches
    tail_twitches = models.BooleanField(
        blank = True
    )

    # Approaches
    approaches = models.BooleanField(
        blank = True
    )

    # Indifferent
    indifferent = models.BooleanField(
        blank = True
    )

    # Runs from
    runs_from = models.BooleanField(
        blank = True
    )

    def __str__(self):
        return self.unique_squirrel_id
