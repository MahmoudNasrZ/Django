import json
from django.core.management.base import BaseCommand # Django's baseclass for creating custom management commands
from myapp.models import ClassArea  # Import the model To Work With 

class Command(BaseCommand): # Import The mangement Base Command From Cors
    help = 'Import ClassArea data from a JSON file' #  short description of the command when using python manage.py help

    #This function allows the script to accept a JSON file path as an argument.
    def add_arguments(self, parser): 
        parser.add_argument('json_file', type=str, help='Path to the JSON file') # json_file will store the path provided when running the command

    def handle(self, *args, **kwargs): # kwargs retrieves the file path provided by the user.
        file_path = kwargs['json_file']
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                class_areas = []  # Use bulk_create for efficiency
                for entry in data:
                    class_areas.append(ClassArea(
                        length=int(entry['length']),
                        width=int(entry['width'])
                    ))

                ClassArea.objects.bulk_create(class_areas)  # Efficient insertion

            self.stdout.write(self.style.SUCCESS('✅ ClassArea data imported successfully!'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'❌ Error: {e}'))
