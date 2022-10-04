from django.shortcuts import render
from django.http import HttpResponse
from .models import item


def index(request):
    objs = item.objects.all()
    return render(request, 'listing/index.html', {"items": objs})

def detail(request, id):
    obj = item.objects.get(pk=id)
    return HttpResponse(obj.item_name)