# Generated by Django 4.2 on 2024-03-17 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Snapp', '0012_foods_list_rename_food_food_reseved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food_reseved',
            name='customer_name',
        ),
    ]
