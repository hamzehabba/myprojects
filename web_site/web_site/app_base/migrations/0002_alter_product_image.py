# Generated by Django 4.2.11 on 2024-09-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/setpic', verbose_name='تصویر محصول:'),
        ),
    ]
