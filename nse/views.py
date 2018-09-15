from django.shortcuts import render
from django.http import HttpResponse
from .models import stocksData
from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def showgraph(request):
    stklist=stocksData.objects.all()
    #print(stklist)
    template = loader.get_template('nse/index.html')
    context = {
        'stock_list': stklist,
    }
    return HttpResponse(template.render(context, request))