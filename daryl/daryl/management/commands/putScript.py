from django.core.management.base import BaseCommand
from daryl.models import *

class Command(BaseCommand):
        args = ''
        help = 'populates our database with images'

        def handle(self, *args, **options):
                data = {
                        'images' : [{
                                'filename': 'img1.jpg',
                                'categoryIndex': 0
                        },
                        {
                                'filename': 'img2.jpg',
                                'categoryIndex': 1
                        },
                        {
                                'filename': 'img3.jpg',
                                'categoryIndex': 2
                        }],
                        'categories': ['A','B','C']
                }
                categories = [Category.objects.create(name = cat) for cat in data['categories']]
                for img in data['images']:
                        filename = img['filename']
                        categoryIndex = img['categoryIndex']
                        Image.objects.create(filename=filename,category=categories[categoryIndex])
