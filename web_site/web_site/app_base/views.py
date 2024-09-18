from django.shortcuts import render
from .models import *

# Create your views here.


def product(request):
    products = Product.published_date.all()

    return products



# def post_list(request):
#     # posts=Post.published.filter(فیلدی که میخواهیم فیلتر کنیم)
#     posts=Post.objects.all()
#     context={
#         'posts':posts,
#     }
#     return render(request, 'template.html',context)