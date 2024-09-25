

from django.urls import path
# from rest_framework.routers import DefaultRouter

from . import test,views

app_name='license_app'

urlpatterns=[
    path('license_api/',test.LicenseViewSet, name='license_api'),
    # path('user_api/',test.UserViewSet, name='user_api'),
    path('user_api/',test.UserViewSet, name='user_api'),
    path('', test.index, name='index'),

]




