from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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
    a=[]
    b=[]
    c=[]
    d=[]
    for i in stklist:
        a.append(i.curtime)
        b.append(i.averageprice)
        c.append(i.buyprice1)
        d.append(i.sellprice1)
    res={
        'ct':a,
        'ap':b,
        'bp':c,
        'sp':d,
    }
    return JsonResponse(res)
    #return HttpResponse(template.render(context, request))