import json
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext, loader
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from daryl.models import *

def test(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render())

def index(request):
	data = json.loads(open('../sample.json').read())
	cnt = 1
	for d in data:
		print(d)

	# Category.clean()
	# Image.clean()
	for cat in data['categories']:
		name = cat
		Category.objects.create(name=name,category_id=cnt)
		# Category.save()
		cnt += 1
	for img in data['images']:
		filename = img['filename']
		category = img['category']
		Image.objects.create(filename=filename,category=category)
		# Image.save()
	image_list = Image.objects.all()
	category_list = Category.objects.all()
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'images': image_list,
		'categories': category_list,
		})
	return HttpResponse(template.render(context))