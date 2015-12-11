import json
from django.views.decorators.csrf import csrf_protect
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

@csrf_protect
def index(request):
    if request.method == 'POST':
        prefix = "category_"
        for k,v in request.POST.iteritems():
            if k.find(prefix) == 0:
                filename = k[len(prefix):]
                categoryName = v
                img = Image.objects.get(filename=filename)
                if img.category.name != categoryName:
                    category = Category.objects.get(name=categoryName)
                    img.category = category
                    img.save();
    image_list = Image.objects.all()
    category_list = Category.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {
    	'images': image_list,
    	'categories': category_list,
    })
    return HttpResponse(template.render(context, request))
