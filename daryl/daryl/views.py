import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext, loader
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

class Image:
	def __init__(self, filename, category):
		self.filename = filename
		self.category = category

	def from_json(self):
		data = json.loads(open('../sample.json').read())['images']
		cnt = 1;
		for cat in data['categories']:
			name = cat['name']
			Category.objects.create(name=name,category_id=cnt)
			Category.save()
			cnt += 1

		for img in data['images']:
			filename = img['filename']
			category = img['category']
			Image.objects.create(filename=filename,category=category)
			Image.save()

def test(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())

def index(request):
	list_image = get_list_or_404(Image)