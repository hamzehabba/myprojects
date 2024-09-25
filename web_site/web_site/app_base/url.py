from django.urls import path
from . import views
from . import products


app_name='app_base'
urlpatterns=[
    # path('product/',views.product, name='product'),
    path('products/', products.productviewset, name='products_api'),
    path('', products.index, name='index'),
]
