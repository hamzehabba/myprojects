from django.http import HttpResponse, JsonResponse

from .models import *
from django.shortcuts import render

def productviewset(request):
    queryset = Product.objects.all()

    product= [x.api() for x in queryset]
    return JsonResponse(product, safe=False)

def index(request):
    f=render(request, 'index.html')
    print(f'sssss{f}')
    return f