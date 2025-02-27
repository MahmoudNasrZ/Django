import json
from django.core.management.base import BaseCommand
from myapp.models import ClassRoom

class Command(BaseCommand):
    help = 'Import ClassRoom data from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['json_file']
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                classrooms = []  # Use bulk_create for efficiency
                for entry in data:
                    classrooms.append(ClassRoom(
                        name=entry['name'],
                        subject=entry['subject'],
                        year=entry['year']
                    ))

                ClassRoom.objects.bulk_create(classrooms)  # Efficient insertion

            self.stdout.write(self.style.SUCCESS('✅ Data imported successfully!'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'❌ Error: {e}'))
