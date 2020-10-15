import csv
import datetime

from django.core.management.base import BaseCommand, CommandError
from sqtracker.models import Sightings


class Command(BaseCommand):
    help = 'An import command'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', help = 'file containing squirrel details')

    def handle(self, *args, **options):
        file_path = options['csv_path']

        try:
            with open(file_path, encoding = 'utf-8') as f:
                reader = csv.DictReader(f)
                for i in reader:
                    data = Sightings(
                        latitude = i['X'],
                        longitude = i['Y'],
                        unique_squirrel_id = i['Unique Squirrel ID'],
                        shift = i['Shift'],
                        date = datetime.datetime.strptime(i['Date'],'%m%d%Y'),
                        age = i['Age'],
                        primary_fur_color = i['Primary Fur Color'],
                        location = i['Location'],
                        specific_location = i['Specific Location'],
                        running = convertBool(i['Running']),
                        chasing = convertBool(i['Chasing']),
                        climbing = convertBool(i['Climbing']),
                        eating = convertBool(i['Eating']),
                        foraging = convertBool(i['Foraging']),
                        other_activities = i['Other Activities'],
                        kuks = convertBool(i['Kuks']),
                        quaas = convertBool(i['Quaas']),
                        moans = convertBool(i['Moans']),
                        tail_flags = convertBool(i['Tail flags']),
                        tail_twitches = convertBool(i['Tail twitches']),
                        approaches = convertBool(i['Approaches']),
                        indifferent = convertBool(i['Indifferent']),
                        runs_from = convertBool(i['Runs from']),
                    )
                    data.save()
            msg = f'You are importing from {file_path}'
            self.stdout.write(self.style.SUCCESS(msg))

        except:
            raise CommandError('Importing file failed')
