from django.http import HttpResponse
from django.template import RequestContext, loader

def test(request):
    template = loader.get_template('test.html')
    return HttpResponse(template.render());

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render());
