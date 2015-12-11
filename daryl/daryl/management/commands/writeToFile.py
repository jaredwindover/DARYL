from django.core.management.base import BaseCommand
from daryl.models import *

class Command(BaseCommand):
    args = ''
    help = 'writes database to a file'
    
    def handle(self, *args, **options):
        filename = "hardcoded.txt"
        file = open(filename, 'w')
        for img in Image.objects.all():
                file.write(img.filename +' ' + str(img.category.id) +  '\n')
