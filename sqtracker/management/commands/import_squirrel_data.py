import csv
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'A help for using the command' #TODO change the help text after

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file containing squirrel details')

    def handle(self, *args, **options):
        file_path = options['squirrel_file']

        try:
            with open(file_path) as f:
                reader = csv.Reader(f)
                for item in reader:
                    #item
                    pass
            msg = f'You are importing from {file_path}'
            self.stdout.write(self.style.SUCCESS(msg))

        except:
            raise CommandError('Import file failed')
