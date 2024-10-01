from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class PostPdmin(admin.ModelAdmin):
    list_display=['title', 'author','published_date']
    name = 'app_base'
    verbose_name = 'اپ اصلی'
#
admin.sites.AdminSite.site_header='پنل مدیریت جنگو'
admin.sites.AdminSite.site_title=' پنل مدیریت '
