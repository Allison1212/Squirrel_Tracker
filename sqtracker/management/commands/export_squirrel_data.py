import csv
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'A help for using the command' #TODO change the help text after

    def add_arguments(self, parser):
        parser.add_argument('export_file', help = 'A path that your file want to export to')

    def handle(self, *args, **options):
        file_path = options['export_file']

        try:
            msg = f'You are exporting to {file_path}'
            self.stdout.write(self.style.SUCCESS(msg))
            # write csv file 
        except:
