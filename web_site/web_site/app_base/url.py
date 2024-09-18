from django.urls import path
from . import views


rlpatterns=[
    # path('',views.index,name='index'),
    path('product/',views.product, name='product')
]
