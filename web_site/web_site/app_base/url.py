from django.urls import path
from . import views
from . import products


app_name='app_base'
urlpatterns=[
    # path('',views.index,name='index'),
    path('product/',views.product, name='product'),
    path('products/', products.productviewset, name='products_api'),
    # path('products/', views.productviewset, name='products_api'),
]
