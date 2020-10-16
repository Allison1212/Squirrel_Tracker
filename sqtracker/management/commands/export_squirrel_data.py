import csv
import datetime
from django.core.management.base import BaseCommand, CommandError
from sqtracker.models import Sightings


class Command(BaseCommand):
    help = 'An export command'

    def add_arguments(self, parser):
        parser.add_argument('export_path', help = 'A path that your file want to export to')

    def handle(self, *args, **options):
        try:
            file_path = options['export_path']
            with open(file_path,'w') as fp:
                sighting_writer = csv.DictWriter(
                    fp,
                    delimiter = ',',
                    fieldnames = [
                        'X',
                        'Y',
                        'Unique Squirrel ID',
                        'Shift',
                        'Date',
                        'Age',
                        'Primary Fur Color',
                        'Location',
                        'Specific Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail flags',
                        'Tail twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs from',
                        ]
                    )
                sighting_writer.writeheader()

                for row in Sightings.objects.all():
                    if row.date:
                        date_form = row.date.strftime('%m%d%Y')
                    else:
                        date_form = row.date
                        
                    sighting_writer.writerow({
                        'X': row.longitude,
                        'Y': row.latitude,
                        'Unique Squirrel ID': row.unique_squirrel_id,
                        'Shift': row.shift,
                        'Date': date_form,
                        'Age': row.age,
                        'Primary Fur Color': row.primary_fur_color,
                        'Location': row.location,
                        'Specific Location': row.specific_location,
                        'Running': row.running,
                        'Chasing': row.chasing,
                        'Climbing': row.climbing,
                        'Eating': row.eating,
                        'Foraging':row.foraging,
                        'Other Activities': row.other_activities,
                        'Kuks': row.kuks,
                        'Quaas': row.quaas,
                        'Moans': row.moans,
                        'Tail flags': row.tail_flags,
                        'Tail twitches': row.tail_twitches,
                        'Approaches': row.approaches,
                        'Indifferent': row.indifferent,
                        'Runs from': row.runs_from
                        })
            msg = f'You are exporting to {file_path}'
            self.stdout.write(self.style.SUCCESS(msg))
        except:
            raise CommandError('Exporting file failed')
