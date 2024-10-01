from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.



def website(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def website1(request):
    return HttpResponse("Hello world!")

