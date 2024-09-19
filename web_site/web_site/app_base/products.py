from django.http import HttpResponse

from .models import *

def productviewset(request):
    queryset = Product.objects.all()

    product= [x.api() for x in queryset]
    return HttpResponse(product)