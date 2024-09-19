from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    author=models.ForeignKey(User,verbose_name='ایجاد کننده:',on_delete=models.CASCADE,related_name='user_product')
    title=models.CharField(max_length=30,verbose_name='عنوان محصول:')
    image=models.ImageField(verbose_name='تصویر محصول:',upload_to='media/setpic')
    price=models.FloatField(verbose_name='قیمت محصول:')
    discription=models.TextField(verbose_name='توضیحات:')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def api(self):
        return {
            'title': self.title,
            'description': self.discription,
            'image':self.image
        }

