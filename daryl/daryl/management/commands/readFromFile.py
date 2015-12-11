from django.core.management.base import BaseCommand
from daryl.models import *

class Command(BaseCommand):
  args = ''
  help = 'writes a file to database'
    
  def handle(self, *args, **options):
    filename = "hardcoded.txt"
    file = open(filename, 'r')
    Image.objects.all().delete()
    for line in file:
      pieces = line.split()
      filename = (' ').join(pieces[:-1])
      id = pieces[-1]
      category = Category.objects.get(id=id)
      Image.objects.create(filename=filename,category=category)
